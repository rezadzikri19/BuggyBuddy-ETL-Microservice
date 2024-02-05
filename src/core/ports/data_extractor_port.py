from abc import ABC, abstractmethod
from typing import Dict, Any

from core.models.base_model import BaseMatrixModel

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self, data: None, fields: Dict[str, Any]) -> BaseMatrixModel:
    pass
  
  @abstractmethod
  def format_raw_data(self, data: BaseMatrixModel) -> BaseMatrixModel:
    pass