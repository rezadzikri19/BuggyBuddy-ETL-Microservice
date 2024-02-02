# fetch raw data from data source
# format raw data
# fetch train data from data source
# format train data
# fetch embedded data from data source
# format embedded data

from abc import ABC, abstractmethod

class ExtractDataUsecaseInterface(ABC):
  @abstractmethod
  def fetch_data(self):
    pass
  
  @abstractmethod
  def format_data(self):
    pass
  
  @abstractmethod
  def validate_data(self):
    pass

class ExtractDataRawUsecase(ExtractDataUsecaseInterface):
  def __init__(self, raw_data_model, data_extract_driver, data_validation_driver, data_memory_save_driver) -> None:
    self.raw_data_model = raw_data_model
    self.data_extract_driver = data_extract_driver
    self.data_validation_driver = data_validation_driver
    self.data_memory_save_driver = data_memory_save_driver
  
  def fetch_data(self, **kwargs):
    fields = {
      'include_fields': [
        'id',
        'duplicates',
        'summary',
        'description',
        'status',
        'resolution',
        'platform',
        'product',
        'priority',
        'severity',
        'component'
        ],
      'product': 'firefox',
    }
    fetched = self.data_extract_driver.get_data_from_source(fields, **kwargs)

    return fetched
  
  def format_data(self, data):   
    formatted = self.data_extract_driver.format_raw_data(data)
    
    return formatted
  
  def validate_data(self, data):
    validated = self.data_validation_driver.validate(data, self.raw_data_model)
    validated = self.data_memory_save_driver.save_memory(validated)
    
    return validated

