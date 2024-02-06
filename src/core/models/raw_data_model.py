from typing import Any, Dict, List, Optional

from core.models.base_model import BaseMatrixModel

class FetchRawData(BaseMatrixModel):
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

class RawDataModel(BaseMatrixModel):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)
    
    self.columns = {
        'bug_id': int,
        'report_type': str,
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
    