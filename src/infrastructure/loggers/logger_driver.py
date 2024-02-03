import logging
import os
from datetime import datetime

from core.ports.logger_port import LoggerPort

class LoggerDriver(LoggerPort):
  _instance = None
  
  def __new__(cls):
      if not cls._instance:
        cls._instance = super(LoggerDriver, cls).__new__(cls)
        cls._instance._initialize()
      return cls._instance
      
  def _initialize(self) -> None:
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(logging.DEBUG)
    
    log_file=f'bank_log_{datetime.now().strftime("%Y-%m-%d")}.log'
    curr_dir = os.getcwd()
    log_path = os.path.join(curr_dir, os.pardir, os.pardir, os.pardir, 'logs', log_file)
    self.log_path = log_path
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    file_handler = logging.FileHandler(log_path, mode='a')
    file_handler.setFormatter(formatter)
    self.logger.addHandler(file_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    self.logger.addHandler(console_handler)

  def log_info(self, message: str) -> None:
    self.logger.info(message)
    
  def log_error(self, message: str) -> None:
    self.logger.error(message)
    
  def close_logger(self) -> None:
    for handler in self.logger.handlers:
      handler.close()