import os
import sys

import pandas as pd
import numpy as np
import pymongo

from typing import List
from dotenv import load_dotenv

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

from Threat_Lens.Entity.Config_Entity import TLDataIngestConfig
from Threat_Lens.Entity.Artifact_Entity import TLDataIngestArtifact

MONGODB_URL = os.getenv("MONGODB_URL")

class TLDataIngest:
  def __init__(self):
    pass

  def export_Collection_as_DF(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  def export_Data2FeatureStore(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  def split_in_Train_Test(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)