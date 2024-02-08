from src.core.services.extract_data_service import ExtractDataRawService
from src.core.services.transform_data_service import TransformDataService
from src.core.services.dump_data_service import DumpDataService

from src.core.usecases.data_pipeline_usecase import DataPipelineUsecase

from src.infrastructure.data_drivers.data_extractor_driver import DataExtractorDriver
from src.infrastructure.data_drivers.data_transformer_driver import DataTransformerDriver
from src.infrastructure.data_drivers.data_loader_driver import DataLoaderDriver

from src.infrastructure.loggers.logger_driver import LoggerDriver

def main():
  logger_driver = LoggerDriver()
  
  data_extractor_driver = DataExtractorDriver(logger_driver)
  data_transformer_driver = DataTransformerDriver(logger_driver)
  data_loader_driver = DataLoaderDriver(logger_driver)
  
  extract_data_service = ExtractDataRawService(
    data_extractor_driver,
    logger_driver)
  transform_data_service = TransformDataService(
    data_transformer_driver,
    logger_driver)
  dump_data_service = DumpDataService(
    data_loader_driver,
    logger_driver)
  
  data_pipeline_usecase = DataPipelineUsecase(
    extract_data_service,
    transform_data_service,
    dump_data_service,
    logger_driver)
  
  result = data_pipeline_usecase.extract_data_pipeline()
  result = data_pipeline_usecase.transform_data_pipeline(result)
  result = data_pipeline_usecase.load_data_pipeline(result)
  
if __name__ == "__main__":
  main()