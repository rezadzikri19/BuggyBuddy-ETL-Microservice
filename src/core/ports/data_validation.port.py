from abc import ABC, abstractmethod

class DataValidatorPort(ABC):
  @abstractmethod
  def format_raw_data(self):
    pass