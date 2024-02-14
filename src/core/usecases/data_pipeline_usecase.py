from ...core.usecases.extract_data_usecase import ExtractDataRawUsecase
from ...core.usecases.transform_data_usecase import TransformDataUsecase
from ...core.usecases.dump_data_usecase import DumpDataUsecase

from ...core.ports.logger_port import LoggerPort
from ...core.ports.message_broker_port import MessageBrokerPort

from ...core.models.base_model import BaseMatrixModel

class DataPipelineUsecase():
  def __init__(
      self,
      data_extract_usecase: ExtractDataRawUsecase,
      data_transform_usecase: TransformDataUsecase,
      data_dump_usecase: DumpDataUsecase,
      message_broker: MessageBrokerPort,
      logger: LoggerPort) -> None:
    self.data_extract_usecase = data_extract_usecase
    self.data_transform_usecase = data_transform_usecase
    self.data_dump_usecase = data_dump_usecase
    self.message_broker = message_broker
    self.logger = logger
  
  
  def extract_data_pipeline(self) -> BaseMatrixModel:
    try:
      result = self.data_extract_usecase.extract_data(data=None)
      self.data_dump_usecase.dump_raw_data(result)
      
      self.message_broker.publish_message(
        exchange='etl_service',
        route='extract_pipeline',
        data={'status': 'SUCCESS', 'message': 'ETL_PIPELINE [EXTRACT] - SUCCESS'})
      self.logger.log_info('ETL_PIPELINE [EXTRACT] - SUCCESS')
      
      return result
    except Exception as error:
      error_message = f'DataPipelineUsecase.extract_data_pipeline: {error}'
      
      self.message_broker.publish_message(
        exchange='etl_service',
        route='extract_pipeline',
        data={'status': 'failed', 'message': f'{error_message}'})
      self.logger.log_error(error_message, error)
  
  
  def transform_data_pipeline(self, data: BaseMatrixModel) -> BaseMatrixModel:
    try:
      result = self.data_transform_usecase.transform_data(data)
      self.data_dump_usecase.dump_processed_data(result)
      
      self.logger.log_info('ETL_PIPELINE [TRANSFORM] - SUCCESS')
      self.message_broker.publish_message(
        exchange='etl_service',
        route='transform_pipeline',
        data={'status': 'SUCCESS', 'message': 'ETL_PIPELINE [TRANSFORM] - SUCCESS'})
      
      return result
    except Exception as error:
      error_message = f'DataPipelineUsecase.extract_data_pipeline: {error}'
      
      self.message_broker.publish_message(
        exchange='etl_service',
        route='transform_pipeline',
        data={'status': 'failed', 'message': f'{error_message}'})
      self.logger.log_error(error_message, error)
  
  
  def load_data_pipeline(self, raw_data: BaseMatrixModel, processed_data: BaseMatrixModel) -> None:
    try:
      self.data_dump_usecase.dump_raw_data(raw_data)
      self.data_dump_usecase.dump_processed_data(processed_data)
      
      self.message_broker.publish_message(
        exchange='etl_service',
        route='load_pipeline',
        data={'status': 'SUCCESS', 'message': 'ETL_PIPELINE [LOAD] - SUCCESS'})
      self.logger.log_info('ETL_PIPELINE [LOAD] - SUCCESS')
    except Exception as error:
      error_message = f'DataPipelineUsecase.load_data_pipeline: {error}'
      
      self.message_broker.publish_message(
        exchange='etl_service',
        route='load_pipeline',
        data={'status': 'failed', 'message': f'{error_message}'})
      self.logger.log_error(error_message, error)
  
  
  def run_pipeline(self) -> None:
    try:
      raw_data = self.extract_data_pipeline()
      processed_data = self.transform_data_pipeline(raw_data)
      
      self.load_data_pipeline(raw_data, processed_data)
      
      self.message_broker.publish_message(
        exchange='etl_service',
        route='all_pipeline',
        data={'status': 'SUCCESS', 'message': 'ETL_PIPELINE [ALL] - SUCCESS'})
      self.logger.log_info('ETL_PIPELINE [ALL] - SUCCESS')
    except Exception as error:
      error_message = f'DataPipelineUsecase.run_pipeline: {error}'
      
      self.message_broker.publish_message(
        exchange='etl_service',
        route='all_pipeline',
        data={'status': 'failed', 'message': f'{error_message}'})
      self.logger.log_error(error_message, error)