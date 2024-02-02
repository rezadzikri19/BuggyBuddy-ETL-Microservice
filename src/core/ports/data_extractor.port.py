from abc import ABC, abstractmethod

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self):
    pass
  
  @abstractmethod
  def format_raw_data(self):
    pass