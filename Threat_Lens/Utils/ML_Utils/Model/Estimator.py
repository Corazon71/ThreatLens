import os
import sys

from Threat_Lens.Constants.Training_Pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME
from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

class TLModel:
  def __init__(self, Preprocessor, Model):
    try:
      self.Preprocessor = Preprocessor
      self.Model = Model
    except Exception as e:
      raise TLException(e, sys)
    
  def predict(self, X):
    try:
      X_transform = self.Preprocessor.transform(X)
      y_hat = self.Model.predict(X_transform)

      return y_hat
    except Exception as e:
      raise TLException(e, sys)
    
class ModelResolver:
  def __init__(self, Model_Dir = SAVED_MODEL_DIR):
    try:
      self.Model_Dir = Model_Dir
    except Exception as e:
      raise TLException(e, sys)
    
  def get_best_model_path(self) -> str:
    try:
      timestamps = list(map(int, os.listdir(self.Model_Dir)))
      latest_TS = max(timestamps)
      latest_Model_Path = os.path.join(self.Model_Dir, f"{latest_TS}", MODEL_FILE_NAME)
      return latest_Model_Path
    except Exception as e:
      raise TLException(e, sys)
    
  def is_model_exist(self) -> bool:
    try:
      if not os.path.exists(self.Model_Dir):
        return False
      
      timestamps = os.listdir(self.Model_Dir)
      if len(timestamps) == 0:
        return False
      
      latest_Model_Path = self.get_best_model_path()

      if not os.path.exists(latest_Model_Path):
        return False
      
      return True
    except Exception as e:
      raise TLException(e, sys)