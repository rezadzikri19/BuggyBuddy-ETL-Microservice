from abc import ABC, abstractmethod

from core.types.common_types import MatrixLike, ArrayLike

class DataMemorySavePort(ABC):
  @abstractmethod
  def save_memory(self, data: MatrixLike) -> MatrixLike:
    pass