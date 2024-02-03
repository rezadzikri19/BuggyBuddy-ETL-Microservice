import requests
import json
import concurrent.futures
from urllib.parse import urlencode
from typing import List

from core.ports.data_extractor_port import DataExtractorPort

import pandas as pd
import numpy as np

class DataExtractorDriver(DataExtractorPort):
  def __init__(self) -> None:
    pass
  
  def fetch_data(url: str, params=None):
    try:
      response = requests.get(url, params=params)
      if (response.status_code == 200):
        return response.json()
      
      print(f"Error response with status code: {response.status_code}")
    except Exception as error:
      print(f'Failed to fetch data: {error}')
      
  def urls_builder(base_url: str, n_fetch: int, limit: int, **kwargs) -> str:
    urls = []
    for i in range(n_fetch):
      param = {
        'offset': i * limit,
        'limit': limit,
        **kwargs,
      }
      
      full_url = base_url + '?' + urlencode(param)
      urls.append(full_url)

    return urls
  
  def get_data_from_source(self, fields):
    base_url = 'https://bugzilla.mozilla.org/rest/bug'
    n_fetch = 50
    limit = 5000

    urls = self.urls_builder(base_url, n_fetch, limit, **fields)
    response_data = []

    max_workers = 50
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
      response_data = list(executor.map(self.fetch_data, urls))
      
    response_data = [item['bugs'] for item in response_data]
    response_data = [item for sublist in response_data for item in sublist]
    
    data = pd.DataFrame(response_data)
    data = data.set_index('id')
    
    return data