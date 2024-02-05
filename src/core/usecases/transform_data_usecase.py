from typing import Dict, Any, Callable, List

from core.ports.data_transformer_port import DataTransformerPort
from core.ports.data_validation_port import DataValidatorPort
from core.ports.logger_port import LoggerPort

from core.models.base_model import BaseMatrixModel
from core.models.transformed_data_model import *

class TransformDataUsecase:
  def __init__(
      self,
      data_transformer: DataTransformerPort,
      data_validator: DataValidatorPort,
      logger: LoggerPort) -> None:
    self.data_transformer = data_transformer
    self.data_validator = data_validator
    self.logger = logger
  
  
  def run_validate_transformer(
      self,
      data: BaseMatrixModel,
      schema_input: Dict[str, Any],
      schema_output: Dict[str, Any],
      transformer: Callable[..., None],
      transformer_args: Dict[str, Any]) -> BaseMatrixModel:
    self.data_validator.validate(data, schema_input)
    result = transformer(**transformer_args)
    self.data_validator.validate(result, schema_output)
    return result


  def drop_features(self, data: BaseMatrixModel, features_to_drop: List[str]) -> BaseMatrixModel:
    try:
      if not features_to_drop:
        raise Exception('features_to_drop cannot be empty!')
      
      result = self.run_validate_transformer(
          data,
          schema_input=DropFeatsInputModel.__annotations__,
          schema_output=DropFeatsOutputModel.__annotations__,
          transformer=self.data_transformer.drop_features,
          transformer_args={'data': data, 'features_to_drop': features_to_drop})
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.drop_features: {error}'
      self.logger.log_error(error_message)
  
  
  def remove_duplicates(self, data: BaseMatrixModel, keep: str = 'first') -> BaseMatrixModel:
    try:     
      result = self.run_validate_transformer(
          data,
          schema_input=RemoveDuplicatesInputModel.__annotations__,
          schema_output=RemoveDuplicatesOutputModel.__annotations__,
          transformer=self.data_transformer.remove_duplicates,
          transformer_args={'data': data, 'keep': keep})
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.remove_duplicates: {error}'
      self.logger.log_error(error_message)


  def aggregate_text_features(self, data: BaseMatrixModel) -> BaseMatrixModel:
    try:      
      result = self.run_validate_transformer(
          data,
          schema_input=AggregateTextInputModel.__annotations__,
          schema_output=AggregateTextoutputModel.__annotations__,
          transformer=self.data_transformer.aggregate_text_features,
          transformer_args={'data': data})
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.aggregate_text_features: {error}'
      self.logger.log_error(error_message)


  def clean_sentences(self, data: BaseMatrixModel) -> BaseMatrixModel:
    try:     
      result = self.run_validate_transformer(
          data,
          schema_input=CleanSentInputModel.__annotations__,
          schema_output=CleanSentOutputModel.__annotations__,
          transformer=self.data_transformer.clean_sentences,
          transformer_args={'data': data})
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.clean_sentences: {error}'
      self.logger.log_error(error_message)
  
  
  def remove_stopwords(self, data: BaseMatrixModel) -> BaseMatrixModel:
    try:      
      result = self.run_validate_transformer(
          data,
          schema_input=RemoveStopsInputModel.__annotations__,
          schema_output=RemoveStopsOutputModel.__annotations__,
          transformer=self.data_transformer.remove_stopwords,
          transformer_args={'data': data})
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.remove_stopwords: {error}'
      self.logger.log_error(error_message)
  
  
  def sentence_embedding(self, data: BaseMatrixModel) -> BaseMatrixModel:
    try:
      result = self.run_validate_transformer(
          data,
          schema_input=SentEmbeddingInputModel.__annotations__,
          schema_output=SentEmbeddingOutputModel.__annotations__,
          transformer=self.data_transformer.sent_embedding,
          transformer_args={'data': data})  
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.sentence_embedding: {error}'
      self.logger.log_error(error_message)
  
  
  def get_duplicates_to(self, data: BaseMatrixModel) -> BaseMatrixModel:
    try:      
      result = self.run_validate_transformer(
          data,
          schema_input=GetDuplicatesToInputModel.__annotations__,
          schema_output=GetDuplicatesToOutputModel.__annotations__,
          transformer=self.data_transformer.get_duplicates_to,
          transformer_args={'data': data})
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.get_duplicates_to: {error}'
      self.logger.log_error(error_message)