class BaseTransformDataError(Exception):
  pass
  
class ValidateTransformerError(BaseTransformDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'ValidateTransformerError: {self.message}'

class DropFeatureError(BaseTransformDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'DropFeatureError: {self.message}'
  
class RemoveDuplicatesError(BaseTransformDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'RemoveDuplicatesError: {self.message}'
  
class AggregateTextError(BaseTransformDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'AggregateTextError: {self.message}'
  
class CleanSentencesError(BaseTransformDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'CleanSentencesError: {self.message}'
  
class RemoveStopwordsError(BaseTransformDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'RemoveStopwordsError: {self.message}'
  
class GetDuplicatesToError(BaseTransformDataError):
  def __init__(self, message) -> None:
    self.message = message
    
  def __str__(self):
    return f'GetDuplicatesToError: {self.message}'