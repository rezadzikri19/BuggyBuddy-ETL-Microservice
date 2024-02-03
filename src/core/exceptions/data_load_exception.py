class BaseLoadDataError(Exception):
  pass

class LoadRawDataError(BaseLoadDataError):
  def __init__(self, message) -> None:
    self.message = message

  def __str__(self):
    return f'LoadRawDataError: {self.message}'
  
class LoadProcessedDataError(BaseLoadDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'LoadProcessedDataError: {self.message}'