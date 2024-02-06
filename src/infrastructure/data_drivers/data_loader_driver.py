import os

from ...core.ports.data_loader_port import DataLoaderPort
from ...core.models.raw_data_model import RawDataModel
from ...core.models.processed_data_model import ProcessedDataModel

from ...infrastructure.utils.data_utils import dataframe_wrapper

class DataLoaderDriver(DataLoaderPort):
  def __init__(self) -> None:
    pass
  
  @dataframe_wrapper
  def dump_raw_data(self, data: RawDataModel) -> None:
    curr_dir = os.getcwd()
    data_path = os.path.join(curr_dir, 'artifacts', 'data', 'raw_data.parquet')
    data.to_parquet(data_path)


  @dataframe_wrapper
  def dump_processed_data(self, data: ProcessedDataModel) -> None:
    curr_dir = os.getcwd()
    data_path = os.path.join(curr_dir, 'artifacts', 'data', 'processed_data.parquet')
    data.to_parquet(data_path)