# fetch raw data from data source
# format raw data
# fetch train data from data source
# format train data
# fetch embedded data from data source
# format embedded data

class ExtractDataRawUsecase():
  def __init__(self, data_extract_driver, data_validation_driver, data_memory_save_driver) -> None:
    self.data_extract_driver = data_extract_driver
    self.data_validation_driver = data_validation_driver
    self.data_memory_save_driver = data_memory_save_driver
  
  def fetch_data(self, **kwargs):
    fields = {
      'include_fields': ['id', 'duplicates', 'summary', 'description', 'status', 'resolution', 'platform', 'product', 'priority', 'severity', 'component'],
      'product': 'firefox',
    }
    result = self.data_extract_driver.get_data_from_source(fields, **kwargs)

    return result
  
  def format_data(self, data):
    output_schema = {}
    
    result = self.data_extract_driver.format_raw_data(data)
    result = self.data_memory_save_driver.save_memory(result)
    
    self.data_validation_driver.validate(result, output_schema)
    
    return result

