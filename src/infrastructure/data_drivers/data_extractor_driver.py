import requests
import concurrent.futures
from urllib.parse import urlencode
from typing import Any, Dict

from core.ports.data_extractor_port import DataExtractorPort
from core.models.raw_data_model import RawDataModel

import pandas as pd
from configs import DATA_SOURCE_BASEURL

from core.types.common_types import ArrayLike, MatrixLike

class DataExtractorDriver(DataExtractorPort):
  def __init__(self) -> None:
    pass
  
  def fetch_data(url: str, params=None):
    response = requests.get(url, params=params)
    return response.json()
      
  def urls_builder(base_url: str, n_fetch: int, limit: int, **kwargs) -> str:
    urls = []
    for i in range(n_fetch):
      param = {'offset': i * limit, 'limit': limit, **kwargs}
      
      full_url = base_url + '?' + urlencode(param)
      urls.append(full_url)

    return urls
  
  def get_data_from_source(self, fields: Dict[str, Any]) -> MatrixLike:
    n_fetch = 50
    limit = 5000

    urls = self.urls_builder(DATA_SOURCE_BASEURL, n_fetch, limit, **fields)
    response_data = []

    max_workers = 50
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
      response_data = list(executor.map(self.fetch_data, urls))
      
    response_data = [item['bugs'] for item in response_data]
    response_data = [item for sublist in response_data for item in sublist]
    
    data = pd.DataFrame(response_data)
    data = data.set_index('id')
    
    return data
  
  def format_raw_data(self, data: MatrixLike) -> MatrixLike:
    model_columns = list[RawDataModel.__annotations__.keys()]
    data_columns = ['id', 'type', 'status', 'product', 'component', 'platform', 'summary', 'description', 'resolution', 'severity', 'priority', 'duplicates']
    
    column_mapper = {key: value for key, value in zip(data_columns, model_columns)}
    data = data.rename(columns=column_mapper)
    
    return data
    