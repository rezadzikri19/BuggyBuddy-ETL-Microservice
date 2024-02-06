import re
from typing import List, Any

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sentence_transformers import SentenceTransformer

from ...core.ports.data_transformer_port import DataTransformerPort
from ...core.models.transformed_data_model import *
from ...core.models.raw_data_model import RawDataModel
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.data_utils import dataframe_wrapper

nltk.download('stopwords')
nltk.download('punkt')

class DataTransformerDriver(DataTransformerPort):  
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger

  @dataframe_wrapper
  def drop_features(self, data: RawDataModel, features_to_drop: List[Any]) -> DropFeatsModel:
    try:
      data = data.drop(columns=features_to_drop, axis=1)
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.drop_features: {error}'
      self.logger.log_error(error_message)
  
  
  @dataframe_wrapper
  def remove_duplicates(self, data: DropFeatsModel, keep: str = 'first') -> RemoveDuplicatesModel:
    try:
      columns = list(data.columns)
      data = data.loc[data.astype(str).drop_duplicates(subset=columns, keep=keep).index]
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.remove_duplicates: {error}'
      self.logger.log_error(error_message)


  @dataframe_wrapper
  def aggregate_text_features(self, data: RemoveDuplicatesModel) -> AggregateTextModel:
    try:
      data['text'] = data['platform'] + ' ' + data['summary'] + ' ' + data['description']
      data = data.drop(columns=['platform', 'summary', 'description'], axis=1)
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.aggregate_text_features: {error}'
      self.logger.log_error(error_message)
  
  
  def remove_special_chars(self, text: str):
    text = text.lower()
    text = re.sub(r'\n|\t|\r|\0', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = re.sub(r'\s$', '', text)
    text = re.sub(r'\s[b-z]\s', ' ', text)
    text = re.sub(r'\s[b-z]\s', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text
  
  
  def remove_stops(self, text: str):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)
  
  
  @dataframe_wrapper
  def clean_sentences(self, data: AggregateTextModel) -> CleanSentModel:
    try:
      data['text_cleaned'] = data['text'].apply(self.remove_special_chars)
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.clean_sentences: {error}'
      self.logger.log_error(error_message)
  
  
  @dataframe_wrapper
  def remove_stopwords(self, data: CleanSentModel) -> RemoveStopsModel:
    try:
      data['text_cleaned'] = data['text'].apply(self.remove_stops)
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.remove_stopwords: {error}'
      self.logger.log_error(error_message)
  
  
  @dataframe_wrapper
  def sent_embedding(self, data: RemoveStopsModel) -> SentEmbeddingModel:
    try:
      sent_embd_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
      data['text_embedded'] = data['text_cleaned'].apply(sent_embd_model.encode).tolist()
      data = data.drop(columns=['text_cleaned'])
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.sent_embedding: {error}'
      self.logger.log_error(error_message)
    
  
  @dataframe_wrapper
  def get_duplicates_to(self, data: SentEmbeddingModel) -> GetDuplicatesToModel:
    try:
      duplicated = data['duplicates'].apply(lambda x: len(x)).sort_values(ascending=False)
      duplicated = duplicated[duplicated > 0]
      
      duplicated = data.loc[duplicated.index, 'duplicates']
      data['duplicates_to'] = -1

      for idx, dups in zip(duplicated.index, duplicated):
        for item in dups:
          data.loc[data.index == item, 'duplicates_to'] = idx

      data = data.drop(columns=['duplicates'])
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.get_duplicates_to: {error}'
      self.logger.log_error(error_message)
    