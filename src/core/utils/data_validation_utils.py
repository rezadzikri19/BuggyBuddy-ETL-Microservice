from ...core.models.base_model import BaseMatrixModel


def validate_data(data: BaseMatrixModel, schema: BaseMatrixModel) -> None:
  if list(data.columns) != schema.columns:
    Exception('Utils.validate_data: invalid data!')


def io_data_validation(schema_input: BaseMatrixModel = None, schema_output: BaseMatrixModel = None):
  def decorator(func):
    def wrapper(self, data: BaseMatrixModel, *args, **kwargs) -> BaseMatrixModel:
        if data is not None and schema_input is not None:
          validate_data(data, schema_input)
        
        data = func(self, data=data, *args, **kwargs)
        
        if data is not None and schema_output is not None:
          validate_data(data, schema_output)
        return data
    return wrapper
  return decorator
    
    