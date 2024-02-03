from abc import ABC, abstractmethod
from typing import Optional

from core.types.common_types import MatrixLike, ArrayLike

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_raw_data(self, data: MatrixLike, excludes: Optional[ArrayLike] = None):
    pass
  
  @abstractmethod
  def dump_processed_data(self, data: MatrixLike, excludes: Optional[ArrayLike] = None):
    pass