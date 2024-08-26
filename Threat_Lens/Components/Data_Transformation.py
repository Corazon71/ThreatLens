import os
import sys

import pandas as pd
import numpy as np

from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from Threat_Lens.Constants.Training_Pipeline import TARGET_COLUMN
from Threat_Lens.Constants.Training_Pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS
from Threat_Lens.Entity.Artifact_Entity import TLDataValidArtifact, TLDataTransformArtifact
from Threat_Lens.Entity.Config_Entity import TLDataTransformConfig
from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging
from Threat_Lens.Utils.Main_Utils.Utils import Save_numpy_array, Save_object

class TLDataTransform:
  def __init__(self, DTConfig : TLDataTransformConfig, DVArtifact : TLDataValidArtifact):
    try:
      self.DataTransformConfig = DTConfig
      self.DataValidArtifact = DVArtifact
    except Exception as e:
      raise TLException(e, sys)
    
  @staticmethod
  def read_Data(FilePath) -> pd.DataFrame:
    try:
      
      return pd.read_csv(FilePath)
    except Exception as e:
      raise TLException(e, sys)
    
  def get_Transformer_Object(cls) -> Pipeline:
    logging.info(f"Entering get_Transformer_Object method of TLDataTransform class")
    try:
      Imptr : KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
      logging.info(f"Initialized KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
      PrPrcssr : Pipeline = Pipeline([("Imputer", Imptr)])
      logging.info(f"Exiting get_Transformer_Object method of TLDataTransform class")

      return PrPrcssr
    except Exception as e:
      raise TLException(e, sys)
    
  def initiate_DataTransformation(self) -> TLDataTransformArtifact:
    try:
      logging.info(f"Starting Data Transformation")

      TrDF = TLDataTransform.read_Data(self.DataValidArtifact.ValTrainFPath)
      TsDF = TLDataTransform.read_Data(self.DataValidArtifact.ValTestFPath)
      Preprocessor = self.get_Transformer_Object()
      logging.info(f"Got the Preprocessor Object")

      Ip_Feature_TrDF = TrDF.drop(columns = [TARGET_COLUMN], axis = 1)
      Trgt_Feature_TrDF = TrDF[TARGET_COLUMN]
      Trgt_Feature_TrDF = Trgt_Feature_TrDF.replace(-1, 0)
      
      Ip_Feature_TsDF = TsDF.drop(columns = [TARGET_COLUMN], axis = 1)
      Trgt_Feature_TsDF = TsDF[TARGET_COLUMN]
      Trgt_Feature_TsDF = Trgt_Feature_TsDF.replace(-1, 0)

      Preprocessor_Obj = Preprocessor.fit(Ip_Feature_TrDF)
      Trnsf_Ip_Feature_TrDF = Preprocessor_Obj.transform(Ip_Feature_TrDF)
      Trnsf_Ip_Feature_TsDF = Preprocessor_Obj.transform(Ip_Feature_TsDF)

      Train_Array = np.c_[Trnsf_Ip_Feature_TrDF, np.array(Trgt_Feature_TrDF)]
      Test_Array = np.c_[Trnsf_Ip_Feature_TsDF, np.array(Trgt_Feature_TsDF)]

      Save_numpy_array(self.DataTransformConfig.TrnsfTrainPath, Array = Train_Array)
      Save_numpy_array(self.DataTransformConfig.TrnsfTestPath, Array = Test_Array)
      Save_object(self.DataTransformConfig.TrnsfObjPath, Preprocessor_Obj)

      DataTransformArtifact = TLDataTransformArtifact(
        TrnsfObjFPath = self.DataTransformConfig.TrnsfObjPath,
        TrnsfTrainFPath = self.DataTransformConfig.TrnsfTrainPath,
        TrnsfTestFPath = self.DataTransformConfig.TrnsfTestPath
      )

      return DataTransformArtifact
    except Exception as e:
      raise TLException(e, sys)