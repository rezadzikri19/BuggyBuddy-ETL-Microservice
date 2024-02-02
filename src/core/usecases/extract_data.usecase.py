# fetch raw data from data source
# format raw data
# fetch train data from data source
# format train data
# fetch embedded data from data source
# format embedded data

from abc import ABC, abstractmethod

class ExtractDataUsecaseInterface(ABC):
  @abstractmethod
  def fetch_data(self):
    pass
  
  @abstractmethod
  def format_data(self):
    pass
  
  @abstractmethod
  def save_data(self):
    pass
  
class ExtractDataRawUsecase(ExtractDataUsecaseInterface):
  def __init__(self) -> None:
    pass
  
  def fetch_data(self):
    pass
  
  def format_data(self):
    pass
  
class ExtractDataTrainUsecase(ExtractDataUsecaseInterface):
  def __init__(self) -> None:
    pass
  
  def fetch_data(self):
    pass
  
  def format_data(self):
    pass
  
class ExtractDataProcessedUsecase(ExtractDataUsecaseInterface):
  def __init__(self) -> None:
    pass
  
  def fetch_data(self):
    pass
  
  def format_data(self):
    pass

