from abc import ABC, abstractmethod
from typing import Dict

class DataValidatorPort(ABC):
  @abstractmethod
  def validate(self, data, schema: Dict[str, type]):
    pass