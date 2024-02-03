from abc import ABC, abstractmethod
from typing import Optional

from core.types.common_types import MatrixLike, ArrayLike

class DataTransformerPort(ABC):
  @abstractmethod
  def impute(self, data: MatrixLike, mode: str, value, excludes: Optional[ArrayLike] = None) -> MatrixLike:
    pass
  
  @abstractmethod
  def drop_features(self, data: MatrixLike, features_to_drop: ArrayLike, excludes: Optional[ArrayLike] = None) -> MatrixLike:
    pass
  
  @abstractmethod
  def remove_duplicates(self, data: MatrixLike, how: str, excludes: Optional[ArrayLike] = None) -> MatrixLike:
    pass
  
  @abstractmethod
  def remove_stopwords(self, data: MatrixLike, excludes: Optional[ArrayLike] = None):
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data: MatrixLike, excludes: Optional[ArrayLike] = None):
    pass
  
  @abstractmethod
  def sent_embedding(self, data: MatrixLike, excludes: Optional[ArrayLike] = None):
    pass
  
  @abstractmethod
  def get_duplicates_to(self, data: MatrixLike, excludes: Optional[ArrayLike] = None):
    pass