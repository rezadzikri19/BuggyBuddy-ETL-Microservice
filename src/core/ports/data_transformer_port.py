from abc import ABC, abstractmethod
from typing import List

from ...core.models.transformed_data_model import TransformedDataModel
from ...core.models.raw_data_model import RawDataModel

from ...core.dtos.data_transform_dto import *

class DataTransformerPort(ABC):
  @abstractmethod
  def remove_duplicates(self, data: RawDataModel, keep: str = 'first') -> RemoveDuplicatesDTO:
    pass
  
  @abstractmethod
  def get_duplicates_to(self, data: RemoveDuplicatesDTO) -> TransformedDataModel:
    pass