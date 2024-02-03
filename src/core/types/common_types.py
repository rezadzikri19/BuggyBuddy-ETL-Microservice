from typing import Union, List, Any

import pandas as pd
import numpy as np

MatrixLike = Union[pd.DataFrame, np.ndarray]
ArrayLike = Union[pd.Series, np.ndarray, List[Any]]