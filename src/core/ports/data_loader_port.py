from abc import ABC, abstractmethod

from ...core.models.raw_data_model import RawDataModel
from ...core.models.processed_data_model import ProcessedDataModel

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_raw_data(self, data: RawDataModel) -> None:
    pass
  
  @abstractmethod
  def dump_processed_data(self, data: ProcessedDataModel) -> None:
    pass