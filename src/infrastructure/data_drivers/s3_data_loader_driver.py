import os
from datetime import datetime
from io import BytesIO

import boto3
import pyarrow as pa
import pyarrow.parquet as pq

from ...core.ports.data_loader_port import DataLoaderPort
from ...core.models.raw_data_model import RawDataModel
from ...core.models.transformed_data_model import TransformedDataModel
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.data_utils import dataframe_wrapper

class S3DataLoaderDriver(DataLoaderPort):
  def __init__(
      self,
      aws_access_key_id: str,
      aws_secret_access_key: str,
      region_name: str,
      bucket_name: str,
      logger: LoggerPort) -> None:
    session = boto3.Session(
      aws_access_key_id=aws_access_key_id,
      aws_secret_access_key=aws_secret_access_key,
      region_name=region_name
    )
    self.s3_client = session.client('s3')
    self.bucket_name = bucket_name
    self.logger = logger
  
  @dataframe_wrapper
  def dump_raw_data(self, data: RawDataModel) -> None:
    try:       
      # file_name = f'/raw_data/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_raw_data.parquet'
      file_name = 'ETL/raw_data/raw_data.parquet'
      buffer = BytesIO()
      
      arrow_table = pa.Table.from_pandas(data)
      pq.write_table(arrow_table, buffer)
      
      buffer.seek(0)
      self.s3_client.upload_fileobj(buffer, self.bucket_name, file_name)
    except Exception as error:
      error_message = f'S3DataLoaderDriver.dump_raw_data: {error}'
      self.logger.log_error(error_message, error)

  @dataframe_wrapper
  def dump_processed_data(self, data: TransformedDataModel) -> None:
    try:
      # file_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_processed_data.parquet'
      file_name = 'ETL/processed_data/processed_data.parquet'
      buffer = BytesIO()
      
      arrow_table = pa.Table.from_pandas(data)
      pq.write_table(arrow_table, buffer)
      
      buffer.seek(0)
      self.s3_client.upload_fileobj(buffer, self.bucket_name, file_name)
    except Exception as error:
      error_message = f'S3DataLoaderDriver.dump_processed_data: {error}'
      self.logger.log_error(error_message, error)