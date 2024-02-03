from abc import ABC, abstractmethod

class DataValidatorPort(ABC):
  @abstractmethod
  def validate(self, data, schema):
    pass