from abc import ABC, abstractmethod
from typing import List

from core.models.base_model import BaseMatrixModel

class DataTransformerPort(ABC):
  @abstractmethod
  def drop_features(self, data: BaseMatrixModel, features_to_drop: List[str]) -> BaseMatrixModel:
    pass
  
  @abstractmethod
  def remove_duplicates(self, data: BaseMatrixModel, keep: str) -> BaseMatrixModel:
    pass
  
  @abstractmethod
  def clean_sentences(self, data: BaseMatrixModel):
    pass
  
  @abstractmethod
  def remove_stopwords(self, data: BaseMatrixModel):
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data: BaseMatrixModel):
    pass
  
  @abstractmethod
  def sent_embedding(self, data: BaseMatrixModel):
    pass
  
  @abstractmethod
  def get_duplicates_to(self, data: BaseMatrixModel):
    pass