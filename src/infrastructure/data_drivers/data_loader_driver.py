import os
import pandas as pd

from core.ports.data_loader_port import DataLoaderPort

from infrastructure.utils.data_utils import dataframe_wrapper

class DataLoaderDriver(DataLoaderPort):
  def __init__(self) -> None:
    pass
  
  @dataframe_wrapper
  def dump_raw_data(self, data: pd.DataFrame):
    curr_dir = os.getcwd()
    data_path = os.path.join(curr_dir, os.pardir, os.pardir, os.pardir, 'artifacts', 'data', 'raw_data.parquet')
    data.to_parquet(data_path)


  @dataframe_wrapper
  def dump_processed_data(self, data: pd.DataFrame):
    curr_dir = os.getcwd()
    data_path = os.path.join(curr_dir, os.pardir, os.pardir, os.pardir, 'artifacts', 'data', 'processed_data.parquet')
    data.to_parquet(data_path)