from typing import List, Optional, Any, Tuple

class BaseMatrixModel:
  def __init__(
      self,
      columns: List[str],
      data: List[List[Any]],
      index: Optional[List[Any]] = None) -> None:
    self.columns = columns
    self.data = data
    self.index = index
    
    if not index:
      self.index = list(range(len(data)))
      
    self.size = self._validate_size(data)
    self.data_types = self._validate_types(data)
  
  def _validate_size(self, data: List[List[Any]]) -> Tuple[int]:
    result = all(len(row) == len(data[0]) for row in data)
    
    if not result:
      raise Exception('BaseMatrixModel._validate_size: incorrect matrix size!')
    
    return (len(data), len(data[0]))
  
  
  def _validate_types(self, data: List[List[Any]]) -> List[type]:
    result = all(all(type(item) == type(row[0]) for item in row) for row in data)
    
    if not result:
      raise Exception('BaseMatrixModel._validate_types: mixing data type found!')

    data_types = [type(row[0]) for row in data]
    return data_types

  
  def __getitem__(self, key):
    if type(key) == list:
      idx, col = key
      col_idx = self.columns.index(col)
      
      return self.data[idx][col_idx]
    
    return self.data[key]



class BaseArrayModel:
  def __init__(
    self,
      column: str,
      data: List[Any],
      index: Optional[List[Any]]) -> None:
    self.column = column
    self.data = data
    self.index = index
    
    if not index:
      self.index = list(range(len(data)))
      
    self.data_type = self._validate_type(data)
  
  
  def _validate_type(self, data: List[Any]) -> None:
    result = all(type(item) == type(data[0]) for item in data)
    
    if not result:
      raise Exception('mixing data type found!')
    
    data_type = type(data[0])
    return data_type
  
  
  def __getitem__(self, idx):
    return self.data[idx]