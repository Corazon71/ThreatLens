import os
import sys
import json

import certifi
import pandas as pd
import numpy as np
import pymongo

from dotenv import load_dotenv

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

MONGODB_URL = os.getenv("MONGODB_URL")
CA = certifi.where()

class DataUpload():
  def __init__(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  def csv2json_converter(self, path):
    try:
      Data = pd.read_csv(path)
      Data.reset_index(drop = True, inplace = True)
      Records = list(json.loads(Data.T.to_json()).values())
      return Records
    except Exception as e:
      raise TLException(e, sys)
    
  def pushing_Data2MongoDB(self, recs, db, cllctn):
    try:
      self.database = db
      self.collection = cllctn
      self.records = recs

      self.mongo_client = pymongo.MongoClient(MONGODB_URL)
      self.database = self.mongo_client[self.database]
      self.collection = self.database[self.collection]
      self.collection.insert_many(self.records)
      return len(self.records)
    except Exception as e:
      raise TLException(e, sys)
    
if __name__ == "__main__":
  DataPath = "./Data/Data.csv"
  Database = "PunkRecords"
  Collection = "TLData"
  Ingst = DataUpload()
  Records = Ingst.csv2json_converter(DataPath)
  NumRecords = Ingst.pushing_Data2MongoDB(Records, Database, Collection)
  print(NumRecords)