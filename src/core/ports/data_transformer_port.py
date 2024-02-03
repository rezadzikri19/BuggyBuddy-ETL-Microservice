from abc import ABC, abstractmethod
from typing import List

class DataTransformerPort(ABC):
  @abstractmethod
  def impute(self, data: str, mode: str, value):
    pass
  
  @abstractmethod
  def drop_features(self, data, features_to_drop: List[str]):
    pass
  
  @abstractmethod
  def remove_duplicates(self, data, how: str):
    pass
  
  @abstractmethod
  def remove_stopwords(self, data):
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data):
    pass
  
  @abstractmethod
  def sent_embedding(self, data):
    pass
  
  @abstractmethod
  def get_duplicates_to(self, data):
    pass