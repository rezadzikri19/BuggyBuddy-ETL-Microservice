class BaseExtractDataError(Exception):
  pass
  
class FetchDataError(BaseExtractDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'FetchDataError: {self.message}'

class FormatDataError(BaseExtractDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'FormatDataError: {self.message}'