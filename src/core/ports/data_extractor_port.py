from abc import ABC, abstractmethod
from typing import Dict, Any

from ...core.models.raw_data_model import RawDataModel

from ...core.dtos.data_extract_dto import FetchRawDataDTO

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self, data: None, fields: Dict[str, Any]) -> FetchRawDataDTO:
    pass
  
  @abstractmethod
  def format_raw_data(self, data: FetchRawDataDTO) -> RawDataModel:
    pass