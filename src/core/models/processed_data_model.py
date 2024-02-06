from typing import List, Optional, Any

from ...core.models.base_model import BaseMatrixModel

class ProcessedDataModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)
    
    self.columns = {
        'bug_id': int,
        'text': int,
        'text_embedded': List[int],
        'duplicates_to': int
      }