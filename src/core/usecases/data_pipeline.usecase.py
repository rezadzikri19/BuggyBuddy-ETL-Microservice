from abc import ABC, abstractmethod

class DataPipelineUsecaseInterface(ABC):
  @abstractmethod
  def run_pipeline(self) -> None:
    pass

class DataPipelineUsecase(DataPipelineUsecaseInterface):
  def __init__(self, data_extract_usecase, data_transform_usecase, data_dump_usecase) -> None:
    self.data_extract_usecase = data_extract_usecase
    self.data_transform_usecase = data_transform_usecase
    self.data_dump_usecase = data_dump_usecase
    pass
  
  def extract_data_pipeline(self):
    result = self.data_extract_usecase.fetch_data()
    result = self.data_extract_usecase.format_data(result)
    
    self.data_dump_usecase.dump_raw_data(result)
    
    return result
  
  def transform_data_pipeline(self, data):
    result = self.data_transform_usecase.impute_missing_values(data, mode='most_frequent')
    result = self.data_transform_usecase.remove_duplicates(result, how='first')
    result = self.data_transform_usecase.aggregate_text_features(result)
    result = self.data_transform_usecase.clean_sentence(result)
    result = self.data_transform_usecase.remove_stopwords(result)
    result = self.data_transform_usecase.sentence_embedding(result)

    return result
  
  def load_data_pipeline(self, data) -> None:
    self.data_dump_usecase.dump_processed_data(data)
  
  def run_pipeline(self) -> None:
    result = self.extract_data_pipeline()
    result = self.transform_data_pipeline(result)
    self.load_data_pipeline(result)