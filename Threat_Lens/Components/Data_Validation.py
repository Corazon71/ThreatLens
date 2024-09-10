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
  def __init__(self, DVConfig : TLDataValidConfig, DIArtifact : TLDataIngestArtifact):
    try:
      self.DataValidConfig = DVConfig
      self.DataIngestArtifact = DIArtifact
      self._Schema_Config = Read_yaml_file(SCHEMA_FILE_PATH)
    except Exception as e:
      raise TLException(e, sys)
    
  @staticmethod
  def read_Data(FilePath) -> pd.DataFrame:
    try:

      return pd.read_csv(FilePath)
    except Exception as e:
      raise TLException(e, sys)
    
  def validate_No_of_Columns(self, DF : pd.DataFrame) -> bool:
    try:
      Num_of_Clmns = len(self._Schema_Config["columns"])
      logging.info(f"Number of required columns : {Num_of_Clmns}")
      logging.info(f"Number of dataframe columns : {len(DF.columns)}")
      if len(DF.columns) == Num_of_Clmns:
        return True
      
      return False
    except Exception as e:
      raise TLException(e, sys)
    
  def is_Numerical_Column_Exist(self, DF : pd.DataFrame) -> bool:
    try:
      Numerical_Clmns = self._Schema_Config["numerical_columns"]
      Dataframe_Clmns = DF.columns
      Num_Clmn_present = True
      missing_Num_Clmns = []
      for Num_Clmn in Numerical_Clmns:
        if Num_Clmn not in Dataframe_Clmns:
          Num_Clmn_present = False
          missing_Num_Clmns.append(Num_Clmn)
      logging.info(f"Missing Numerical Columns are : {missing_Num_Clmns}")

      return Num_Clmn_present
    except Exception as e:
      raise TLException(e, sys)
  
  def detect_Data_Drift(self, BaseDF, CurrentDF, Threshold = 0.05) -> bool:
    try:
      Status = True
      Report = {}
      for Clmn in BaseDF.columns:
        d1 = BaseDF[Clmn]
        d2 = CurrentDF[Clmn]
        is_same_dist = ks_2samp(d1, d2)
        if Threshold <= is_same_dist.pvalue:
          is_found = False
        else:
          is_found = True
          Status = False
        Report.update({Clmn : {"p_value" : float(is_same_dist.pvalue), "drift_status" : is_found}})

      DRFilePath = self.DataValidConfig.DRFilePath

      DirPath = os.path.dirname(DRFilePath)
      os.makedirs(DirPath, exist_ok = True)
      Write_yaml_file(FPath = DRFilePath, Content = Report)

      return Status
    except Exception as e:
      raise TLException(e, sys)
    
  def initiate_DataValidation(self) -> TLDataValidArtifact:
    try:
      TrFPath = self.DataIngestArtifact.TrainFPath
      TsFPath = self.DataIngestArtifact.TestFPath

      TrDF = TLDataValid.read_Data(TrFPath)
      TsDF = TLDataValid.read_Data(TsFPath)

      Status = self.validate_No_of_Columns(DF = TrDF)
      if not Status:
        ErrMsg = f"{ErrMsg}Train dataframe does not contain all columns.\n"
      Status = self.validate_No_of_Columns(DF = TsDF)
      if not Status:
        ErrMsg = f"{ErrMsg}Test dataframe does not contain all columns.\n"
      
      Status = self.detect_Data_Drift(BaseDF = TrDF, CurrentDF = TsDF)

      DirPath = os.path.dirname(self.DataValidConfig.ValidTrainPath)
      os.makedirs(DirPath, exist_ok = True)
      TrDF.to_csv(self.DataValidConfig.ValidTrainPath, index = False, header = True)
      TsDF.to_csv(self.DataValidConfig.ValidTestPath, index = False, header = True)     
       
      DataValidArtifact = TLDataValidArtifact(
        ValStatus = Status,
        ValTrainFPath = self.DataIngestArtifact.TrainFPath,
        ValTestFPath = self.DataIngestArtifact.TestFPath,
        InvalTrainFPath = None,
        InvalTestFPath = None,
        DriftReportFPath = self.DataValidConfig.DRFilePath
      )

      return DataValidArtifact
    except Exception as e:
      raise TLException(e, sys)
