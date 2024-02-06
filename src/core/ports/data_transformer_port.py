from abc import ABC, abstractmethod
from typing import List

from core.models.transformed_data_model import *
from core.models.raw_data_model import RawDataModel

class DataTransformerPort(ABC):
  @abstractmethod
  def drop_features(self, data: RawDataModel, features_to_drop: List[str]) -> DropFeatsModel:
    pass
  
  @abstractmethod
  def remove_duplicates(self, data: DropFeatsModel, keep: str = 'first') -> RemoveDuplicatesModel:
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data: RemoveDuplicatesModel) -> AggregateTextModel:
    pass
  
  @abstractmethod
  def clean_sentences(self, data: AggregateTextModel) -> CleanSentModel:
    pass
  
  @abstractmethod
  def remove_stopwords(self, data: CleanSentModel) -> RemoveStopsModel:
    pass
  
  @abstractmethod
  def sent_embedding(self, data: RemoveStopsModel) -> SentEmbeddingModel:
    pass
  
  @abstractmethod
  def get_duplicates_to(self, data: SentEmbeddingModel) -> GetDuplicatesToModel:
    pass