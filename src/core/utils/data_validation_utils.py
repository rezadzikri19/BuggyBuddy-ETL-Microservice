from core.models.base_model import BaseMatrixModel


def validate_data(data: BaseMatrixModel, schema: BaseMatrixModel) -> None:
  if not data.columns == schema.columns:
    Exception('DataValidationUsecase.validate_data: invalid data!')


def io_data_validation(schema_input: None, schema_output: None):
  def decorator(func):
    def wrapper(self, data: BaseMatrixModel, *args, **kwargs) -> BaseMatrixModel:
        if data and schema_input: validate_data(data, schema_input)
        
        data = func(self, data=data, *args, **kwargs)
        
        if data and schema_output: validate_data(data, schema_output)
        return data
    return wrapper
  return decorator
    
    