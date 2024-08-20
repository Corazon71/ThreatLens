import os
import sys

import pandas as pd
import numpy as np
import pymongo

from typing import List
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

from Threat_Lens.Entity.Config_Entity import TLDataIngestConfig
from Threat_Lens.Entity.Artifact_Entity import TLDataIngestArtifact

MONGODB_URL = os.getenv("MONGODB_URL")

class TLDataIngest:
  def __init__(self, DataIngestConfig : TLDataIngestConfig):
    self.DataIngestConfig = DataIngestConfig

  def export_Collection_as_DF(self):
    try:
      DatabaseName = self.DataIngestConfig.DatabaseName
      CollectionName = self.DataIngestConfig.DatabaseName

      self.MongoClient = pymongo.mongo_client(MONGODB_URL)
      Collection = self.MongoClient[DatabaseName][CollectionName]

      DF = pd.DataFrame(list(Collection.find()))
      if "_id" in DF.columns.to_list():
        DF = DF.drop(columns = ["_id"], axis = 1)

      DF.replace({"na" : np.nan}, inplace = True)

      return DF
    except Exception as e:
      raise TLException(e, sys)
    
  def export_Data2FeatureStore(self, DF : pd.DataFrame):
    try:
      FS_FilePath = self.DataIngestConfig.FS_FilePath
      DIRPath = os.path.dirname(FS_FilePath)
      os.makedirs(DIRPath, exist_ok = True)
      DF.to_csv(FS_FilePath, index = False, header = True)

      return DF
    except Exception as e:
      raise TLException(e, sys)
    
  def split_in_Train_Test(self, DF : pd.DataFrame):
    try:
      Train, Test = train_test_split(DF, test_size = self.DataIngestConfig.TTSRatio)
      logging.info("Data is split into Train & Test.")

      DIRPath = os.path.dirname(self.DataIngestConfig.TrainPath)
      os.makedirs(DIRPath, exist_ok = True)
      logging.info(f"Exporting Train & Test file path.")

      Train.to_csv(self.DataIngestConfig.TrainPath, index = False, header = True)
      Test.to_csv(self.DataIngestConfig.TestPath, index = False, header = True)
      logging.info(f"Exported Train & Test file path.")
      
    except Exception as e:
      raise TLException(e, sys)

  def initiate_DataIngestion(self):
    try:
      DF = self.export_Collection_as_DF()
      DF = self.export_Data2FeatureStore(DF)
      self.split_in_Train_Test(DF)

      DataIngestArtifact = TLDataIngestArtifact(
        TrainPath = self.DataIngestConfig.TrainPath, 
        TestPath = self.DataIngestConfig.TestPath
      )

      return DataIngestArtifact

    except Exception as e:
      raise TLException(e, sys)