from dataclasses import dataclass
from typing import List, Optional, Any

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
  
  
  def __getitem__(self, idx):
    return self.data[idx]



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
  
  
  def __getitem__(self, idx):
    return self.data[idx]