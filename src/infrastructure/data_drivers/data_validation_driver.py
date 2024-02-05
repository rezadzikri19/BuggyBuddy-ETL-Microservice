from typing import Dict
from collections import Counter

from core.ports.data_validation_port import DataValidatorPort
from core.types.common_types import MatrixLike

class DataValidationDriver(DataValidatorPort):
  def __init__(self) -> None:
    pass
  
  
  def equal_list(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    return counter1 == counter2
  
  
  def validate(self, data: MatrixLike, schema: Dict[str, type]) -> None:
    expected_columns = list(schema.keys())
    data_columns = list(data.columns)
    
    if not self.equal_list(expected_columns, data_columns):
      raise Exception('incorrect data schema!')