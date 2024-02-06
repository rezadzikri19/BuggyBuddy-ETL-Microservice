from typing import List, Optional, Any

from ...core.models.base_model import BaseMatrixModel


class DropFeatsModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)
    
    self.columns = {
        'bug_id': int,
        'platform': str,
        'summary': str,
        'description': str,
        'duplicates': List[int]
      }



class RemoveDuplicatesModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'platform': str,
        'summary': str,
        'description': str,
        'duplicates': List[int]
      }
    


class AggregateTextModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'duplicates': List[int]
      }
    


class CleanSentModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'text_cleaned': str,
        'duplicates': List[int]
      }



class RemoveStopsModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'text_cleaned': str,
        'duplicates': List[int]
      }



class SentEmbeddingModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'embedded_text': List[int],
        'duplicates': List[int]
      }
  


class GetDuplicatesToModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'embedded_text': List[int],
        'duplicates_to': int
      }