import re
from typing import List, Any

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sentence_transformers import SentenceTransformer

from core.ports.data_transformer_port import DataTransformerPort
from core.models.base_model import BaseMatrixModel

from infrastructure.utils.data_utils import dataframe_wrapper

nltk.download('stopwords')
nltk.download('punkt')

class DataTransformerDriver(DataTransformerPort):
  def __init__(self) -> None:
    pass

  @dataframe_wrapper
  def drop_features(self, data: pd.DataFrame, features_to_drop: List[Any]) -> pd.DataFrame:
    data = data.drop(columns=features_to_drop, axis=1)
    return data
  
  
  @dataframe_wrapper
  def remove_duplicates(self, data: pd.DataFrame, keep: str) -> pd.DataFrame:
    columns = list(data.columns)
    data = data.drop_duplicates(subset=columns, keep=keep)
    return data


  @dataframe_wrapper
  def aggregate_text_features(self, data: pd.DataFrame) -> pd.DataFrame:
    data['text'] = data['platform'] + ' ' + data['summary'] + ' ' + data['description']
    data = data.drop(columns=['platform', 'summary', 'description'], axis=1)
    return data
  
  
  def remove_special_chars(text: str):
    text = text.lower()
    text = re.sub(r'\n|\t|\r|\0', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = re.sub(r'\s$', '', text)
    text = re.sub(r'\s[b-z]\s', ' ', text)
    text = re.sub(r'\s[b-z]\s', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text
  
  
  def remove_stopwords(text: str):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)
  
  
  @dataframe_wrapper
  def clean_sentences(self, data: pd.DataFrame) -> pd.DataFrame:
    data['text_cleaned'] = data['text'].apply(self.remove_special_chars)
    return data
  
  
  @dataframe_wrapper
  def sent_embedding(self, data: pd.DataFrame) -> pd.DataFrame:
    sent_embd_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    data['text_embedded'] = data['text'].apply(sent_embd_model.encode)
    return data
    
  
  @dataframe_wrapper
  def get_duplicates_to(self, data: pd.DataFrame) -> pd.DataFrame:
    duplicated = data['duplicates'].apply(lambda x: len(x)).sort_values(ascending=False)
    duplicated = duplicated[duplicated > 0]
    
    duplicated = data.loc[duplicated.index, 'duplicates']
    data['duplicates_to'] = -1

    for idx, dups in zip(duplicated.index, duplicated):
      for item in dups:
        data.loc[data.index == item, 'duplicates_to'] = idx

    data = data.drop(columns=['duplicates'])
    return data
    