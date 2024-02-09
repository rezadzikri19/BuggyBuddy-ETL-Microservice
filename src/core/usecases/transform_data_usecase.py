from ...core.ports.data_transformer_port import DataTransformerPort
from ...core.ports.logger_port import LoggerPort

from ...core.utils.data_validation_utils import io_data_validation

from ...core.models.raw_data_model import RawDataModel
from ...core.dtos.data_transform_dto import *

class TransformDataUsecase:
  def __init__(
      self,
      data_transformer: DataTransformerPort,
      logger: LoggerPort) -> None:
    self.data_transformer = data_transformer
    self.logger = logger
  
  
  @io_data_validation(schema_input=RawDataModel(), schema_output=RemoveDuplicatesDTO())
  def remove_duplicates(self, data: RawDataModel, keep: str = 'first') -> RemoveDuplicatesDTO:
    try:
      result = self.data_transformer.remove_duplicates(data, keep=keep)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.remove_duplicates: {error}'
      self.logger.log_error(error_message, error)


  @io_data_validation(schema_input=RemoveDuplicatesDTO(), schema_output=GetDuplicatesToDTO())
  def get_duplicates_to(self, data: RemoveDuplicatesDTO) -> GetDuplicatesToDTO:
    try:
      result = self.data_transformer.get_duplicates_to(data)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.get_duplicates_to: {error}'
      self.logger.log_error(error_message, error)