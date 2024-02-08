from ...core.services.extract_data_service import ExtractDataRawService
from ...core.services.transform_data_service import TransformDataService
from ...core.services.dump_data_service import DumpDataService

from ...core.ports.logger_port import LoggerPort

from ...core.models.base_model import BaseMatrixModel

class DataPipelineUsecase():
  def __init__(
      self,
      data_extract_usecase: ExtractDataRawService,
      data_transform_usecase: TransformDataService,
      data_dump_usecase: DumpDataService,
      logger: LoggerPort) -> None:
    self.data_extract_usecase = data_extract_usecase
    self.data_transform_usecase = data_transform_usecase
    self.data_dump_usecase = data_dump_usecase
    self.logger = logger
  
  
  def extract_data_pipeline(self) -> BaseMatrixModel:
    result = self.data_extract_usecase.fetch_data(data=None)
    result = self.data_extract_usecase.format_data(result)

    self.data_dump_usecase.dump_raw_data(result)
    self.logger.log_info('ETL_PIPELINE [EXTRACT] - DONE')
    return result
  
  
  def transform_data_pipeline(self, data: BaseMatrixModel) -> BaseMatrixModel:
    result = self.data_transform_usecase.drop_unused_features(data)
    result = self.data_transform_usecase.remove_duplicates(result, keep='first')
    result = self.data_transform_usecase.aggregate_text_features(result)
    result = self.data_transform_usecase.clean_sentences(result)
    result = self.data_transform_usecase.remove_stopwords(result)
    result = self.data_transform_usecase.sentence_embedding(result)
    result = self.data_transform_usecase.get_duplicates_to(result)

    self.logger.log_info('ETL_PIPELINE [TRANSFORM] - DONE')
    return result
  
  
  def load_data_pipeline(self, data: BaseMatrixModel) -> None:
    self.data_dump_usecase.dump_processed_data(data)
    self.logger.log_info('ETL_PIPELINE [LOAD] - DONE')
  
  
  def run_pipeline(self) -> None:
    result = self.extract_data_pipeline()
    result = self.transform_data_pipeline(result)
    self.load_data_pipeline(result)
    self.logger.log_info('ETL_PIPELINE [ALL] - DONE')