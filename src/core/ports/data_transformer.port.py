from abc import ABC, abstractmethod

class DataTransformer(ABC):
  @abstractmethod
  def impute(self, data: str, mode: str, value):
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