# dump raw data
# dump processed data

class DumpData():
  def __init__(self, data_loader_driver) -> None:
    self.data_loader_driver = data_loader_driver
    
  def dump_raw_data(self, data):
    self.data_loader_driver.dump_raw_data(data)
  
  def dump_processed_data(self, data):
    self.data_loader_driver.dump_processed_data(data)