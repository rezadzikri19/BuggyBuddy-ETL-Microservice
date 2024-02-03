from typing import Dict, Any, Callable, List
from core.ports.data_transformer_port import DataTransformerPort
from core.ports.data_validation_port import DataValidatorPort
from core.models.transformed_data_model import *

class TransformDataUsecase:
  def __init__(
      self,
      data_transform_driver: DataTransformerPort,
      data_validation_driver: DataValidatorPort) -> None:
    self.data_transform_driver = data_transform_driver
    self.data_validation_driver = data_validation_driver
  
  def run_validate_transformer(
      self, data,
      schema_input: dict[str, Any],
      schema_output: dict[str, Any],
      transformer: Callable[..., None],
      transformer_args: Dict[str, Any]):
    self.data_validation_driver.validate(data, schema_input)
    result = transformer(**transformer_args)
    self.data_validation_driver.validate(result, schema_output)
    
    return result

  def drop_features(self, data, features_to_drop: List[str]):
    args = {'data': data, 'features_to_drop': features_to_drop}
    
    if not features_to_drop:
      raise Exception('features_to_drop cannot be empty!')
    
    result = self.run_validate_transformer(
        data,
        schema_input=DropFeatsInputModel.__annotations__,
        schema_output=DropFeatsOutputModel.__annotations__,
        pipeline=self.data_transform_driver.impute,
        pipeline_args=args)

    return result
  
  def impute_missing_values(self, data, mode: str ='most_frequent', value=None):
    args = {'data': data, 'mode': mode, 'value': value}
    
    result = self.run_validate_transformer(
        data,
        schema_input=ImputeInputModel.__annotations__,
        schema_output=ImputeOutputModel.__annotations__,
        pipeline=self.data_transform_driver.impute,
        pipeline_args=args)

    return result
  
  def remove_duplicates(self, data, how: str = 'first'):
    args = {'data': data, 'how': how}
    
    result = self.run_validate_transformer(
        data,
        schema_input=RemoveDuplicatesInputModel.__annotations__,
        schema_output=RemoveDuplicatesOutputModel.__annotations__,
        pipeline=self.data_transform_driver.remove_duplicates,
        pipeline_args=args)
    
    return result

  def aggregate_text_features(self, data):
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=AggregateTextInputModel.__annotations__,
        schema_output=AggregateTextoutputModel.__annotations__,
        pipeline=self.data_transform_driver.aggregate_text_features,
        pipeline_args=args)
    
    return result

  def clean_sentences(self, data):
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=CleanSentInputModel.__annotations__,
        schema_output=CleanSentOutputModel.__annotations__,
        pipeline=self.data_validation_driver.validate,
        pipeline_args=args)
    
    return result
  
  def remove_stopwords(self, data):
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=RemoveStopsInputModel.__annotations__,
        schema_output=RemoveStopsOutputModel.__annotations__,
        pipeline=self.data_transform_driver.remove_stopwords,
        pipeline_args=args)
    
    return result
  
  def sentence_embedding(self, data):
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=SentEmbeddingInputModel.__annotations__,
        schema_output=SentEmbeddingOutputModel.__annotations__,
        pipeline=self.data_transform_driver.sent_embedding,
        pipeline_args=args)  
    
    return result
  
  def get_duplicates_to(self, data):
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=GetDuplicatesToInputModel.__annotations__,
        schema_output=GetDuplicatesToOutputModel.__annotations__,
        pipeline=self.data_transform_driver.get_duplicates_to,
        pipeline_args=args)
    
    return result