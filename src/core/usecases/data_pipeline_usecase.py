from core.usecases.extract_data_usecase import ExtractDataRawUsecase
from core.usecases.transform_data_usecase import TransformDataUsecase
from core.usecases.dump_data_usecase import DumpDataUsecase
from core.ports.logger_port import LoggerPort

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
  
  
  def extract_data_pipeline(self):
    result = self.data_extract_usecase.fetch_data()
    result = self.data_extract_usecase.format_data(result)

    self.data_dump_usecase.dump_raw_data(result)
    self.logger.log_info('ETL_PIPELINE [EXTRACT] - SUCCESS')
    return result
  
  
  def transform_data_pipeline(self, data):
    result = self.data_transform_usecase.drop_features(data, features_to_drop=['status', 'priority', 'resolution', 'severity', 'component', 'product', 'report_type'])
    result = self.data_transform_usecase.remove_duplicates(result, how='first')
    result = self.data_transform_usecase.aggregate_text_features(result)
    result = self.data_transform_usecase.clean_sentences(result)
    result = self.data_transform_usecase.remove_stopwords(result)
    result = self.data_transform_usecase.sentence_embedding(result)
    result = self.data_transform_usecase.get_duplicates_to(result)
    result = self.data_transform_usecase.drop_features(data, features_to_drop=['duplicates'])

    self.logger.log_info('ETL_PIPELINE [TRANSFORM] - SUCCESS')
    return result
  
  
  def load_data_pipeline(self, data) -> None:
    self.data_dump_usecase.dump_processed_data(data)
    self.logger.log_info('ETL_PIPELINE [LOAD] - SUCCESS')
  
  
  def run_pipeline(self) -> None:
    result = self.extract_data_pipeline()
    result = self.transform_data_pipeline(result)
    self.load_data_pipeline(result)
    self.logger.log_info('ETL_PIPELINE [ALL] - SUCCESS')