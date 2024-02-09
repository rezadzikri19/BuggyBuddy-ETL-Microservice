from ...core.usecases.extract_data_usecase import ExtractDataRawUsecase
from ...core.usecases.transform_data_usecase import TransformDataUsecase
from ...core.usecases.dump_data_usecase import DumpDataUsecase

from ...core.ports.logger_port import LoggerPort

from ...core.models.base_model import BaseMatrixModel

class DataPipelineUsecase():
  def __init__(
      self,
      data_extract_usecase: ExtractDataRawUsecase,
      data_transform_usecase: TransformDataUsecase,
      data_dump_usecase: DumpDataUsecase,
      logger: LoggerPort) -> None:
    self.data_extract_usecase = data_extract_usecase
    self.data_transform_usecase = data_transform_usecase
    self.data_dump_usecase = data_dump_usecase
    self.logger = logger
  
  
  def extract_data_pipeline(self) -> BaseMatrixModel:
    result = self.data_extract_usecase.extract_data(data=None)
    self.data_dump_usecase.dump_raw_data(result)
    
    self.logger.log_info('ETL_PIPELINE [EXTRACT] - DONE')
    return result
  
  
  def transform_data_pipeline(self, data: BaseMatrixModel) -> BaseMatrixModel:
    result = self.data_transform_usecase.transform_data(data)
    self.data_dump_usecase.dump_processed_data(result)
    
    self.logger.log_info('ETL_PIPELINE [TRANSFORM] - DONE')
    return result
  
  
  def load_data_pipeline(self, raw_data: BaseMatrixModel, processed_data: BaseMatrixModel) -> None:
    self.data_dump_usecase.dump_raw_data(raw_data)
    self.data_dump_usecase.dump_processed_data(processed_data)
    self.logger.log_info('ETL_PIPELINE [LOAD] - DONE')
  
  
  def run_pipeline(self) -> None:
    raw_data = self.extract_data_pipeline()
    processed_data = self.transform_data_pipeline(raw_data)
    
    self.load_data_pipeline(raw_data, processed_data)
    self.logger.log_info('ETL_PIPELINE [ALL] - DONE')