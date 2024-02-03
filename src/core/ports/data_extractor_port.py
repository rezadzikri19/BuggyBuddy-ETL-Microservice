from abc import ABC, abstractmethod
from typing import Dict, Any

from core.types.common_types import MatrixLike, ArrayLike

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self, fields: Dict[str, Any]) -> MatrixLike:
    pass
  
  @abstractmethod
  def format_raw_data(self, data: MatrixLike) -> MatrixLike:
    pass