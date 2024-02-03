from abc import ABC, abstractmethod
from typing import Optional

from core.types.common_types import MatrixLike, ArrayLike

class DataMemorySavePort(ABC):
  @abstractmethod
  def save_memory(self, data: MatrixLike, excludes: Optional[ArrayLike] = None) -> MatrixLike:
    pass