from core.models.raw_data_model import RawDataModel
from core.ports.data_extractor_port import DataExtractorPort
from core.ports.data_validation_port import DataValidatorPort
from core.ports.logger_port import LoggerPort
from core.models.base_model import BaseMatrixModel

class ExtractDataRawUsecase():
  def __init__(
      self,
      data_extractor: DataExtractorPort,
      data_validator: DataValidatorPort,
      logger: LoggerPort) -> None:
    self.data_extractor = data_extractor
    self.data_validator = data_validator
    self.logger = logger
  
  
  def fetch_data(self):
    try:
      fields = {
        'include_fields': ['id', 'duplicates', 'summary', 'description', 'status', 'resolution', 'platform', 'product', 'priority', 'severity', 'component'],
        'product': 'firefox',
      }
      result = self.data_extractor.get_data_from_source(fields=fields)
      return result
    except Exception as error:
      error_message = f'ExtractDataRawUsecase.fetch_data: {error}'
      self.logger.log_error(error_message)
  
  
  def format_data(self, data: BaseMatrixModel):
    try:
      result = self.data_extractor.format_raw_data(data)      
      self.data_validator.validate(result, RawDataModel.__annotations__)
      return result
    except Exception as error:
      error_message = f'ExtractDataRawUsecase.format_data: {error}'
      self.logger.log_error(error_message)

