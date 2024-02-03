# impute missing value
# remove duplicates
# clean sentence
# remove stopwords
# aggregate text features
# sentence embedding

class TransformDataUsecase:
  def __init__(self, data_transform_driver, data_validation_driver) -> None:
    self.data_transform_driver = data_transform_driver
    self.data_validation_driver = data_validation_driver
  
  def run_validate_transformer(self, data, schema_input, schema_output, transformer, transformer_args):
    self.data_validation_driver.validate(data, schema_input)
    result = transformer(**transformer_args)
    self.data_validation_driver.validate(result, schema_output)
    
    return result
  
  def impute_missing_values(self, data, mode='most_frequent', value=None):
    schema_input = {}
    schema_output = {}
    args = {'data': data, 'mode': mode, 'value': value}
    
    result = self.run_validate_transformer(
        data,
        schema_input=schema_input,
        schema_output=schema_output,
        pipeline=self.data_transform_driver.impute,
        pipeline_args=args)

    return result
  
  def remove_duplicates(self, data, how='first'):
    schema_input = {}
    schema_output = {}
    args = {'data': data, 'how': how}
    
    result = self.run_validate_transformer(
        data,
        schema_input=schema_input,
        schema_output=schema_output,
        pipeline=self.data_transform_driver.remove_duplicates,
        pipeline_args=args)
    
    return result
  
  def clean_sentences(self, data):
    schema_input = {}
    schema_output = {}
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=schema_input,
        schema_output=schema_output,
        pipeline=self.data_validation_driver.validate,
        pipeline_args=args)
    
    return result
  
  def remove_stopwords(self, data):
    schema_input = {}
    schema_output = {}
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=schema_input,
        schema_output=schema_output,
        pipeline=self.data_transform_driver.remove_stopwords,
        pipeline_args=args)
    
    return result
  
  def aggregate_features(self, data):
    schema_input = {}
    schema_output = {}
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=schema_input,
        schema_output=schema_output,
        pipeline=self.data_transform_driver.aggregate_text_features,
        pipeline_args=args)
    
    return result
  
  def sentence_embedding(self, data):
    schema_input = {}
    schema_output = {}
    args = {'data': data}
    
    result = self.run_validate_transformer(
        data,
        schema_input=schema_input,
        schema_output=schema_output,
        pipeline=self.data_transform_driver.sent_embedding,
        pipeline_args=args)  
    
    return result