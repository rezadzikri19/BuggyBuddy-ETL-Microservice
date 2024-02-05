from abc import ABC, abstractmethod

from core.models.base_model import BaseMatrixModel

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_raw_data(self, data: BaseMatrixModel) -> None:
    pass
  
  @abstractmethod
  def dump_processed_data(self, data: BaseMatrixModel) -> None:
    pass