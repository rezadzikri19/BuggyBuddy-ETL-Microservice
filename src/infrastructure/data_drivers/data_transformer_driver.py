from ...core.ports.data_transformer_port import DataTransformerPort
from ...core.ports.logger_port import LoggerPort

from ...core.models.transformed_data_model import *
from ...core.models.raw_data_model import RawDataModel
from ...core.dtos.data_transform_dto import *

from ...infrastructure.utils.data_utils import dataframe_wrapper

class DataTransformerDriver(DataTransformerPort):  
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger


  @dataframe_wrapper
  def remove_duplicates(self, data: RawDataModel, keep: str = 'first') -> RemoveDuplicatesDTO:
    try:
      columns = list(data.columns)
      data = data.loc[data.astype(str).drop_duplicates(subset=columns, keep=keep).index]
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.remove_duplicates: {error}'
      self.logger.log_error(error_message, error)

  
  @dataframe_wrapper
  def get_duplicates_to(self, data: RemoveDuplicatesDTO) -> GetDuplicatesToDTO:
    try:
      duplicated = data['duplicates'].apply(lambda x: len(x)).sort_values(ascending=False)
      duplicated = duplicated[duplicated > 0]
      
      duplicated = data.loc[duplicated.index, 'duplicates']
      data['duplicates_to'] = -1

      for idx, dups in zip(duplicated.index, duplicated):
        for item in dups:
          data.loc[data.index == item, 'duplicates_to'] = idx

      data = data.drop(columns=['duplicates'])
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.get_duplicates_to: {error}'
      self.logger.log_error(error_message, error)
    