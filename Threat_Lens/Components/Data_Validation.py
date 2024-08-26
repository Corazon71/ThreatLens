import os
import sys

import pandas as pd

from Threat_Lens.Constants.Training_Pipeline import SCHEMA_FILE_PATH
from Threat_Lens.Entity.Artifact_Entity import TLDataIngestArtifact, TLDataValidArtifact
from Threat_Lens.Entity.Config_Entity import TLDataValidConfig
from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging
from Threat_Lens.Utils.Main_Utils.Utils import Read_yaml_file, Write_yaml_file
from scipy.stats import ks_2samp

class TLDataValid:
  def __init__(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  @staticmethod
  def read_Data(FilePath) -> pd.DataFrame:
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  def validate_No_of_Columns(self, DF : pd.DataFrame) -> bool:
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  def is_Numerical_Column_Exist(self, DF : pd.DataFrame) -> bool:
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
  
  def detect_Data_Drift(self, BaseDF, CurrentDF, Threshold = 0.05) -> bool:
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  def initiate_DataValidation(self) -> TLDataValidArtifact:
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
