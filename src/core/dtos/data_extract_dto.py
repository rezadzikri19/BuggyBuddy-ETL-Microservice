from typing import Any, List, Optional

from ...core.models.base_model import BaseMatrixModel

class FetchRawDataDTO(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)
    
    self.columns = {
        'id': int,
        'type': str,
        'status': str,
        'product': str,
        'component': str,
        'platform': str,
        'summary': str,
        'description': str,
        'resolution': str,
        'severity': str,
        'priority': str,
        'duplicates': List[int]
      }