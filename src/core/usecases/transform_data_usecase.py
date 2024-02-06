from core.ports.data_transformer_port import DataTransformerPort
from core.ports.logger_port import LoggerPort

from core.utils.data_validation_utils import io_data_validation

from core.models.raw_data_model import RawDataModel
from core.models.transformed_data_model import *

class TransformDataUsecase:
  def __init__(
      self,
      data_transformer: DataTransformerPort,
      logger: LoggerPort) -> None:
    self.data_transformer = data_transformer
    self.logger = logger
    

  @io_data_validation(schema_input=RawDataModel(), schema_output=DropFeatsModel())
  def drop_unused_features(self, data: RawDataModel) -> DropFeatsModel:
    try:
      features_to_drop = ['status', 'priority', 'resolution', 'severity', 'component', 'product', 'report_type']
      
      result = self.data_transformer.drop_features(data, features_to_drop=features_to_drop)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.drop_features: {error}'
      self.logger.log_error(error_message)
  
  
  @io_data_validation(schema_input=DropFeatsModel(), schema_output=RemoveDuplicatesModel())
  def remove_duplicates(self, data: DropFeatsModel, keep: str = 'first') -> RemoveDuplicatesModel:
    try:
      result = self.data_transformer.remove_duplicates(data, keep=keep)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.remove_duplicates: {error}'
      self.logger.log_error(error_message)


  @io_data_validation(schema_input=RemoveDuplicatesModel(), schema_output=AggregateTextModel())
  def aggregate_text_features(self, data: RemoveDuplicatesModel) -> AggregateTextModel:
    try:
      result = self.data_transformer.aggregate_text_features(data)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.aggregate_text_features: {error}'
      self.logger.log_error(error_message)


  @io_data_validation(schema_input=AggregateTextModel(), schema_output=CleanSentModel())
  def clean_sentences(self, data: AggregateTextModel) -> CleanSentModel:
    try:
      result = self.data_transformer.clean_sentences(data)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.clean_sentences: {error}'
      self.logger.log_error(error_message)


  @io_data_validation(schema_input=CleanSentModel(), schema_output=RemoveStopsModel())
  def remove_stopwords(self, data: CleanSentModel) -> RemoveStopsModel:
    try:
      result = self.data_transformer.remove_stopwords(data)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.remove_stopwords: {error}'
      self.logger.log_error(error_message)
  
  
  @io_data_validation(schema_input=RemoveStopsModel(), schema_output=SentEmbeddingModel())
  def sentence_embedding(self, data: RemoveStopsModel) -> SentEmbeddingModel:
    try:
      result = self.data_transformer.sent_embedding(data) 
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.sentence_embedding: {error}'
      self.logger.log_error(error_message)
  
  
  @io_data_validation(schema_input=SentEmbeddingModel(), schema_output=GetDuplicatesToModel())
  def get_duplicates_to(self, data: SentEmbeddingModel) -> GetDuplicatesToModel:
    try:
      result = self.data_transformer.get_duplicates_to(data)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.get_duplicates_to: {error}'
      self.logger.log_error(error_message)