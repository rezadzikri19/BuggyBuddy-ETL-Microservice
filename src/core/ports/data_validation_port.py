from abc import ABC, abstractmethod
from typing import Dict, Optional

from core.types.common_types import MatrixLike, ArrayLike

class DataValidatorPort(ABC):
  @abstractmethod
  def validate(self, data: MatrixLike, schema: Dict[str, type], excludes: Optional[ArrayLike] = None):
    pass