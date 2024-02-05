from typing import Dict

from core.models.base_model import BaseMatrixModel

class DataValidationUsecase():
  def __init__(self) -> None:
    pass
  
  
  def validate_data(self, data: BaseMatrixModel, schema: Dict[str, type]) -> None:
    expected_columns = list(schema.keys())
    data_columns = list(data.columns)
    
    columns = [col for col in expected_columns if col in data_columns]
    
    if len(columns) != len(expected_columns) or len(columns) != len(data_columns):
      raise Exception('incorrect column name(s) found!')
    
    is_valid = all(type(data[[0, col]]) == schema[col] for col in columns)
    
    if not is_valid:
      raise Exception('incorrect data type(s) found!')
    
    