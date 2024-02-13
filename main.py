import os
from dotenv import load_dotenv

from src.core.usecases.extract_data_usecase import ExtractDataRawUsecase
from src.core.usecases.transform_data_usecase import TransformDataUsecase
from src.core.usecases.dump_data_usecase import DumpDataUsecase

from src.core.usecases.data_pipeline_usecase import DataPipelineUsecase

from src.infrastructure.data_drivers.mozilla_data_extractor_driver import MozillaDataExtractorDriver
from src.infrastructure.data_drivers.pandas_data_transformer_driver import PandasDataTransformerDriver
from src.infrastructure.data_drivers.local_data_loader_driver import LocalDataLoaderDriver
from src.infrastructure.data_drivers.s3_data_loader_driver import S3DataLoaderDriver

from src.infrastructure.loggers.logger_driver import LoggerDriver

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')
BUCKET_NAME = os.getenv('BUCKET_NAME')

def main():
  logger_driver = LoggerDriver()
  
  data_extractor_driver = MozillaDataExtractorDriver(logger_driver)
  data_transformer_driver = PandasDataTransformerDriver(logger_driver)
  data_loader_driver = S3DataLoaderDriver(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME,
    bucket_name=BUCKET_NAME
  )
  # data_loader_driver = LocalDataLoaderDriver(logger_driver)
  
  extract_data_service = ExtractDataRawUsecase(data_extractor_driver, logger_driver)
  transform_data_service = TransformDataUsecase(data_transformer_driver, logger_driver)
  dump_data_service = DumpDataUsecase(data_loader_driver, logger_driver)
  data_pipeline_usecase = DataPipelineUsecase(extract_data_service, transform_data_service, dump_data_service, logger_driver)
  
  data_pipeline_usecase.run_pipeline()

if __name__ == "__main__":
  main()