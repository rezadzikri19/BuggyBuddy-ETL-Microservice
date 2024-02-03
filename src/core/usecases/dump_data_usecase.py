from core.ports.data_loader_port import DataLoaderPort
from core.ports.logger_port import LoggerPort

class DumpDataUsecase():
  def __init__(
      self,
      data_loader_driver: DataLoaderPort,
      logger_driver: LoggerPort) -> None:
    self.data_loader_driver = data_loader_driver
    self.logger_driver = logger_driver
    
  def dump_raw_data(self, data):
    try:
      self.data_loader_driver.dump_raw_data(data)
    except Exception as error:
      error_message = f'DumpDataUsecase.dump_raw_data: {error}'
      self.logger_driver.log_error(error_message)
        
  def dump_processed_data(self, data):
    try:
      self.data_loader_driver.dump_processed_data(data)
    except Exception as error:
      error_message = f'DumpDataUsecase.dump_processed_data: {error}'
      self.logger_driver.log_error(error_message)