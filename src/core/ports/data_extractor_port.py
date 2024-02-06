from abc import ABC, abstractmethod
from typing import Dict, Any

from core.models.raw_data_model import FetchRawData, RawDataModel

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self, data: None, fields: Dict[str, Any]) -> FetchRawData:
    pass
  
  @abstractmethod
  def format_raw_data(self, data: FetchRawData) -> RawDataModel:
    pass