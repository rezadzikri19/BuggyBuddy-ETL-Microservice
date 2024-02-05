import os

from core.ports.data_loader_port import DataLoaderPort
from core.types.common_types import MatrixLike

class DataLoaderDriver(DataLoaderPort):
  def __init__(self) -> None:
    pass
  
  
  def dump_raw_data(self, data: MatrixLike):
    curr_dir = os.getcwd()
    data_path = os.path.join(curr_dir, os.pardir, os.pardir, os.pardir, 'artifacts', 'data', 'raw_data.parquet')
    data.to_parquet(data_path)


  def dump_processed_data(self, data: MatrixLike):
    curr_dir = os.getcwd()
    data_path = os.path.join(curr_dir, os.pardir, os.pardir, os.pardir, 'artifacts', 'data', 'processed_data.parquet')
    data.to_parquet(data_path)