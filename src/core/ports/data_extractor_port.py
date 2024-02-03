from abc import ABC, abstractmethod
from typing import Dict, Any

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self, fields: Dict[str, Any]):
    pass
  
  @abstractmethod
  def format_raw_data(self, data):
    pass