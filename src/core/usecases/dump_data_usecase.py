from core.ports.data_loader_port import DataLoaderPort

class DumpDataUsecase():
  def __init__(self, data_loader_driver: DataLoaderPort) -> None:
    self.data_loader_driver = data_loader_driver
    
  def dump_raw_data(self, data):
    self.data_loader_driver.dump_raw_data(data)
  
  def dump_processed_data(self, data):
    self.data_loader_driver.dump_processed_data(data)