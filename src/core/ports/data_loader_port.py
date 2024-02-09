from abc import ABC, abstractmethod

from ...core.models.raw_data_model import RawDataModel
from ...core.models.transformed_data_model import TransformedDataModel

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_raw_data(self, data: RawDataModel) -> None:
    pass
  
  @abstractmethod
  def dump_processed_data(self, data: TransformedDataModel) -> None:
    pass