from abc import ABC, abstractmethod

class LoggerPort(ABC):
  @abstractmethod
  def log_info(self, message: str) -> None:
    pass
  
  @abstractmethod
  def log_error(self, message: str) -> None:
    pass