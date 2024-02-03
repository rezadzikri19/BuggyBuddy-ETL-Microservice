from core.models.raw_data_model import RawDataModel
from core.ports.data_extractor_port import DataExtractorPort
from core.ports.data_validation_port import DataValidatorPort
from core.ports.data_memory_save_port import DataMemorySavePort

class ExtractDataRawUsecase():
  def __init__(
      self,
      data_extract_driver: DataExtractorPort,
      data_validation_driver: DataValidatorPort,
      data_memory_save_driver: DataMemorySavePort) -> None:
    self.data_extract_driver = data_extract_driver
    self.data_validation_driver = data_validation_driver
    self.data_memory_save_driver = data_memory_save_driver
  
  def fetch_data(self):
    fields = {
      'include_fields': ['id', 'duplicates', 'summary', 'description', 'status', 'resolution', 'platform', 'product', 'priority', 'severity', 'component'],
      'product': 'firefox',
    }
    result = self.data_extract_driver.get_data_from_source(fields)

    return result
  
  def format_data(self, data):
    result = self.data_extract_driver.format_raw_data(data)
    result = self.data_memory_save_driver.save_memory(result)
    
    self.data_validation_driver.validate(result, RawDataModel.__annotations__)
    
    return result

