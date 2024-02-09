from ...core.ports.data_transformer_port import DataTransformerPort
from ...core.ports.logger_port import LoggerPort

from ...core.utils.data_validation_utils import io_data_validation

from ...core.models.raw_data_model import RawDataModel
from ...core.models.transformed_data_model import TransformedDataModel

class TransformDataUsecase:
  def __init__(
      self,
      data_transformer: DataTransformerPort,
      logger: LoggerPort) -> None:
    self.data_transformer = data_transformer
    self.logger = logger
  
  
  @io_data_validation(schema_input=RawDataModel(), schema_output=TransformedDataModel())
  def transform_data(self, data: RawDataModel) -> TransformedDataModel:
    try:
      result = self.data_transformer.remove_duplicates(data, keep='first')
      result = self.data_transformer.get_duplicates_to(result)
      return result
    except Exception as error:
      error_message = f'TransformDataUsecase.transform_data: {error}'
      self.logger.log_error(error_message, error)