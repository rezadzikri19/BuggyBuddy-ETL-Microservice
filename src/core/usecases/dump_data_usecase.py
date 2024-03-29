from ...core.ports.data_loader_port import DataLoaderPort
from ...core.ports.logger_port import LoggerPort

from ...core.models.raw_data_model import RawDataModel
from ...core.models.transformed_data_model import TransformedDataModel

from ...core.utils.data_validation_utils import io_data_validation

class DumpDataUsecase():
  def __init__(
      self,
      data_loader: DataLoaderPort,
      logger: LoggerPort) -> None:
    self.data_loader = data_loader
    self.logger = logger
    
  
  @io_data_validation(schema_input=RawDataModel())
  def dump_raw_data(self, data: RawDataModel):
    try:
      self.data_loader.dump_raw_data(data)
    except Exception as error:
      error_message = f'DumpDataUsecase.dump_raw_data: {error}'
      self.logger.log_error(error_message, error)
        
  
  @io_data_validation(schema_input=TransformedDataModel())
  def dump_processed_data(self, data: TransformedDataModel):
    try:
      self.data_loader.dump_processed_data(data)
    except Exception as error:
      error_message = f'DumpDataUsecase.dump_processed_data: {error}'
      self.logger.log_error(error_message, error)