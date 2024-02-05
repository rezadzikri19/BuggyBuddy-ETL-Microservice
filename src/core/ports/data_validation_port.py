from abc import ABC, abstractmethod
from typing import Dict

from core.models.base_model import BaseMatrixModel

class DataValidatorPort(ABC):
  @abstractmethod
  def validate(self, data: BaseMatrixModel, schema: Dict[str, type]) -> None:
    pass