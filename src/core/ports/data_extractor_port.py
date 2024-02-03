from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

from core.types.common_types import MatrixLike, ArrayLike

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self, fields: Dict[str, Any], excludes: Optional[ArrayLike] = None) -> MatrixLike:
    pass
  
  @abstractmethod
  def format_raw_data(self, data: MatrixLike, excludes: Optional[ArrayLike] = None) -> MatrixLike:
    pass