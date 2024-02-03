from typing import Dict, Any, Callable, List

from core.ports.data_transformer_port import DataTransformerPort
from core.ports.data_validation_port import DataValidatorPort
from core.models.transformed_data_model import *
from core.ports.logger_port import LoggerPort

class TransformDataUsecase:
  def __init__(
      self,
      data_transform_driver: DataTransformerPort,
      data_validation_driver: DataValidatorPort,
      logger_driver: LoggerPort) -> None:
    self.data_transform_driver = data_transform_driver
    self.data_validation_driver = data_validation_driver
    self.logger_driver = logger_driver
  
  def run_validate_transformer(
      self, data,
      schema_input: Dict[str, Any],
      schema_output: Dict[str, Any],
      transformer: Callable[..., None],
      transformer_args: Dict[str, Any]):
    self.data_validation_driver.validate(data, schema_input)
    result = transformer(**transformer_args)
    self.data_validation_driver.validate(result, schema_output)

    return result

  def drop_features(self, data, features_to_drop: List[str]):
    try:
      args = {'data': data, 'features_to_drop': features_to_drop}

      if not features_to_drop:
        raise Exception('features_to_drop cannot be empty!')
      
      result = self.run_validate_transformer(
          data,
          schema_input=DropFeatsInputModel.__annotations__,
          schema_output=DropFeatsOutputModel.__annotations__,
          pipeline=self.data_transform_driver.drop_features,
          pipeline_args=args)

      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.drop_features: {error}'
      self.logger_driver.log_error(error_message)
  
  def remove_duplicates(self, data, keep: str = 'first'):
    try:
      args = {'data': data, 'keep': keep}
      
      result = self.run_validate_transformer(
          data,
          schema_input=RemoveDuplicatesInputModel.__annotations__,
          schema_output=RemoveDuplicatesOutputModel.__annotations__,
          pipeline=self.data_transform_driver.remove_duplicates,
          pipeline_args=args)
      
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.remove_duplicates: {error}'
      self.logger_driver.log_error(error_message)

  def aggregate_text_features(self, data):
    try:
      args = {'data': data}
      
      result = self.run_validate_transformer(
          data,
          schema_input=AggregateTextInputModel.__annotations__,
          schema_output=AggregateTextoutputModel.__annotations__,
          pipeline=self.data_transform_driver.aggregate_text_features,
          pipeline_args=args)
      
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.aggregate_text_features: {error}'
      self.logger_driver.log_error(error_message)

  def clean_sentences(self, data):
    try:
      args = {'data': data}
      
      result = self.run_validate_transformer(
          data,
          schema_input=CleanSentInputModel.__annotations__,
          schema_output=CleanSentOutputModel.__annotations__,
          pipeline=self.data_transform_driver.clean_sentences,
          pipeline_args=args)
      
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.clean_sentences: {error}'
      self.logger_driver.log_error(error_message)
  
  def remove_stopwords(self, data):
    try:
      args = {'data': data}
      
      result = self.run_validate_transformer(
          data,
          schema_input=RemoveStopsInputModel.__annotations__,
          schema_output=RemoveStopsOutputModel.__annotations__,
          pipeline=self.data_transform_driver.remove_stopwords,
          pipeline_args=args)
      
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.remove_stopwords: {error}'
      self.logger_driver.log_error(error_message)
  
  def sentence_embedding(self, data):
    try:
      args = {'data': data}

      result = self.run_validate_transformer(
          data,
          schema_input=SentEmbeddingInputModel.__annotations__,
          schema_output=SentEmbeddingOutputModel.__annotations__,
          pipeline=self.data_transform_driver.sent_embedding,
          pipeline_args=args)  
      
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.sentence_embedding: {error}'
      self.logger_driver.log_error(error_message)
  
  def get_duplicates_to(self, data):
    try:
      args = {'data': data}
      
      result = self.run_validate_transformer(
          data,
          schema_input=GetDuplicatesToInputModel.__annotations__,
          schema_output=GetDuplicatesToOutputModel.__annotations__,
          pipeline=self.data_transform_driver.get_duplicates_to,
          pipeline_args=args)
      
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.get_duplicates_to: {error}'
      self.logger_driver.log_error(error_message)