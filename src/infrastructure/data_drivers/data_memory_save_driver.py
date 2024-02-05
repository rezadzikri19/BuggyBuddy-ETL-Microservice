from typing import Optional

import numpy as np

from core.ports.data_memory_save_port import DataMemorySavePort
from core.types.common_types import ArrayLike, MatrixLike

class DataMemorySaveDriver(DataMemorySavePort):
  def __init__(self) -> None:
    pass
  
  
  def is_convertable_sr(self, col: ArrayLike) -> bool:
    if col.dtype == np.int64 \
        and col.max() <= np.iinfo(np.int32).max \
        and col.min() >= np.iinfo(np.int32).min: return True
    
    if col.dtype == np.float64 \
        and col.max() <= np.finfo(np.float32).max \
        and col.min() >= np.finfo(np.float32).min: return True
    
    if np.isnan(col.max()): return True
    return False
  
  
  def save_memory(self, data: MatrixLike, excludes: Optional[ArrayLike]) -> MatrixLike:
    int_cols = list(data.select_dtypes(np.int64).columns)
    float_cols = list(data.select_dtypes(np.float64).columns)
    
    if excludes:
      int_cols = [col for col in int_cols if col not in excludes]
      float_cols = [col for col in float_cols if col not in excludes]
    
    int_cols = [col for col in int_cols if self.is_convertable_sr(data[col])]
    float_cols = [col for col in float_cols if self.is_convertable_sr(data[col])]
    
    int_cols = {col: np.int32 for col in int_cols}
    float_cols = {col: np.float32 for col in float_cols}

    data = data.astype(int_cols)
    data = data.astype(float_cols)
    return data