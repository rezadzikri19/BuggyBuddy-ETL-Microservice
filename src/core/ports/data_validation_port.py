from abc import ABC, abstractmethod
from typing import Dict

from core.types.common_types import MatrixLike, ArrayLike

class DataValidatorPort(ABC):
  @abstractmethod
  def validate(self, data: MatrixLike, schema: Dict[str, type]):
    pass