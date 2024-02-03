from dataclasses import dataclass
from typing import List

from core.models.raw_data_model import RawDataModel 

@dataclass
class DropFeatsInputModel(RawDataModel):
  pass
@dataclass
class DropFeatsOutputModel:
  bug_id: int
  platform: str
  summary: str
  description: str
  duplicates: List[int]


@dataclass
class ImputeInputModel(DropFeatsOutputModel):
  pass
@dataclass
class ImputeOutputModel(DropFeatsOutputModel):
  pass


@dataclass
class RemoveDuplicatesInputModel(DropFeatsOutputModel):
  pass
@dataclass
class RemoveDuplicatesOutputModel(DropFeatsOutputModel):
  pass


@dataclass
class AggregateTextInputModel(DropFeatsOutputModel):
  pass
@dataclass
class AggregateTextoutputModel():
  bug_id: int
  text: str
  duplicates: List[int]
  

@dataclass
class CleanSentInputModel(AggregateTextoutputModel):
  pass
@dataclass
class CleanSentOutputModel():
  bug_id: int
  text: str
  duplicates: List[int]
  cleaned_text: str


@dataclass
class RemoveStopsInputModel(CleanSentOutputModel):
  pass
@dataclass
class RemoveStopsOutputModel(CleanSentOutputModel):
  pass


@dataclass
class SentEmbeddingInputModel(CleanSentOutputModel):
  pass
@dataclass
class SentEmbeddingOutputModel():
  bug_id: int
  text: str
  duplicates: List[int]
  cleaned_text: str
  embedded_text: List[int]
  
  
@dataclass
class GetDuplicatesToInputModel(SentEmbeddingOutputModel):
  pass
@dataclass
class GetDuplicatesToOutputModel():
  bug_id: int
  text: str
  embedded_text: List[int]
  duplicates_to: int