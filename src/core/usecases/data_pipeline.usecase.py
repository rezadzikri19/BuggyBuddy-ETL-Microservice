from abc import ABC, abstractmethod

class DataPipelineUsecaseInterface(ABC):
  @abstractmethod
  def run_pipeline(self) -> None:
    pass

class DataPipelineUsecase(DataPipelineUsecaseInterface):
  def __init__(self) -> None:
    pass
  
  def extract_data_pipeline(self):
    pass
  
  def transform_data_pipeline(self):
    pass
  
  def load_data_pipeline(self):
    pass
  
  def run_pipeline(self) -> None:
    pass