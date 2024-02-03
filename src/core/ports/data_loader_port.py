from abc import ABC, abstractmethod

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_raw_data(self, data):
    pass
  
  @abstractmethod
  def dump_processed_data(self, data):
    pass