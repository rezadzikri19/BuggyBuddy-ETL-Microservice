from core.ports.data_loader_port import DataLoaderPort
from core.ports.logger_port import LoggerPort
from core.models.base_model import BaseMatrixModel

class DumpDataUsecase():
  def __init__(
      self,
      data_loader: DataLoaderPort,
      logger: LoggerPort) -> None:
    self.data_loader = data_loader
    self.logger = logger
    
    
  def dump_raw_data(self, data: BaseMatrixModel):
    try:
      self.data_loader.dump_raw_data(data)
    except Exception as error:
      error_message = f'DumpDataUsecase.dump_raw_data: {error}'
      self.logger.log_error(error_message)
        
        
  def dump_processed_data(self, data: BaseMatrixModel):
    try:
      self.data_loader.dump_processed_data(data)
    except Exception as error:
      error_message = f'DumpDataUsecase.dump_processed_data: {error}'
      self.logger.log_error(error_message)