# dump raw data
# dump train data
# dump processed data

from abc import ABC, abstractmethod

class DumpDataUsecaseInterface(ABC):
  @abstractmethod 
  def dump_data(self):
    pass
  
  @abstractmethod
  def format_data(self):
    pass
  
class DumpDataRawUsecase(DumpDataUsecaseInterface):
  def __init__(self) -> None:
    pass
  
  def dump_data(self):
    pass
  
  def format_data(self):
    pass
  
class DumpDataTrainUsecase(DumpDataUsecaseInterface):
  def __init__(self) -> None:
    pass
  
  def dump_data(self):
    pass
  
  def format_data(self):
    pass
  
class DumpDataProcessedUsecase(DumpDataUsecaseInterface):
  def __init__(self) -> None:
    pass
  
  def dump_data(self):
    pass
  
  def format_data(self):
    pass