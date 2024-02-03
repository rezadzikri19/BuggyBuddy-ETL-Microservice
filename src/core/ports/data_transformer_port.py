from abc import ABC, abstractmethod

from core.types.common_types import MatrixLike, ArrayLike

class DataTransformerPort(ABC):
  @abstractmethod
  def drop_features(self, data: MatrixLike, features_to_drop: ArrayLike) -> MatrixLike:
    pass
  
  @abstractmethod
  def remove_duplicates(self, data: MatrixLike, keep: str) -> MatrixLike:
    pass
  
  @abstractmethod
  def clean_sentences(self, data: MatrixLike):
    pass
  
  @abstractmethod
  def remove_stopwords(self, data: MatrixLike):
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data: MatrixLike):
    pass
  
  @abstractmethod
  def sent_embedding(self, data: MatrixLike):
    pass
  
  @abstractmethod
  def get_duplicates_to(self, data: MatrixLike):
    pass