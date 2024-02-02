from abc import ABC, abstractmethod

class DataMemorySavePort(ABC):
  @abstractmethod
  def save_memory(self):
    pass