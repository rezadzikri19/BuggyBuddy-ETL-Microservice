import concurrent.futures
from typing import Any, Dict

from ...core.ports.data_extractor_port import DataExtractorPort
from ...core.models.raw_data_model import RawDataModel
from ...core.ports.logger_port import LoggerPort
from ...core.dtos.data_extract_dto import FetchRawDataDTO

from ...infrastructure.utils.data_utils import dataframe_wrapper

import pandas as pd
import requests

class DataExtractorDriver(DataExtractorPort):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
  
  
  def fetch_data(self, url: str, params=None):
    response = requests.get(url, params=params)
    return response.json()
  
  
  @dataframe_wrapper
  def get_data_from_source(self, data: None, fields: Dict[str, Any]) -> FetchRawDataDTO:
    try:
      base_url = 'https://bugzilla.mozilla.org/rest/bug'
      n_fetch = 10
      limit = 1000

      params = [{'offset': i * limit, 'limit': limit, **fields} for i in range(n_fetch)]
      
      response_data = []
      max_workers = 25
      with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        response_data = list(executor.map(lambda param: self.fetch_data(base_url, param), params))
        
      response_data = [item['bugs'] for item in response_data]
      response_data = [item for sublist in response_data for item in sublist]
      
      data = pd.DataFrame(response_data)
      data = data.set_index('id')
      return data
    except Exception as error:
      error_message = f'DataExtractorDriver.get_data_from_source: {error}'
      self.logger.log_error(error_message, error)
        
  
  @dataframe_wrapper
  def format_raw_data(self, data: FetchRawDataDTO) -> RawDataModel:
    try:
      model_columns = list(RawDataModel().columns.keys())
      data_columns = ['id', 'type', 'status', 'product', 'component', 'platform', 'summary', 'description', 'resolution', 'severity', 'priority', 'duplicates']
      
      column_mapper = {key: value for key, value in zip(data_columns, model_columns)}
      data = data.rename(columns=column_mapper)
      return data
    except Exception as error:
      error_message = f'DataExtractorDriver.format_raw_data: {error}'
      self.logger.log_error(error_message, error)