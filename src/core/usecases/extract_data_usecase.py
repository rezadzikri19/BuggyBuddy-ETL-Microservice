from ...core.ports.data_extractor_port import DataExtractorPort
from ...core.ports.logger_port import LoggerPort

from ...core.models.raw_data_model import RawDataModel
from ...core.dtos.data_extract_dto import FetchRawDataDTO

from ...core.utils.data_validation_utils import io_data_validation

class ExtractDataRawUsecase():
  def __init__(
      self,
      data_extractor: DataExtractorPort,
      logger: LoggerPort) -> None:
    self.data_extractor = data_extractor
    self.logger = logger
  
  
  @io_data_validation(schema_output=FetchRawDataDTO())
  def fetch_data(self, data: None = None) -> FetchRawDataDTO:
    try:
      fields = {
        'include_fields': ['id', 'duplicates', 'summary', 'description', 'status', 'resolution', 'platform', 'product', 'priority', 'severity', 'component', 'type'],
        'product': 'firefox',
      }
      result = self.data_extractor.get_data_from_source(fields=fields, data=data)
      return result
    except Exception as error:
      error_message = f'ExtractDataRawUsecase.fetch_data: {error}'
      self.logger.log_error(error_message, error)
  
  
  @io_data_validation(schema_input=FetchRawDataDTO(), schema_output=RawDataModel())
  def format_data(self, data: FetchRawDataDTO) -> RawDataModel:
    try:
      result = self.data_extractor.format_raw_data(data)
      return result
    except Exception as error:
      error_message = f'ExtractDataRawUsecase.format_data: {error}'
      self.logger.log_error(error_message, error)

