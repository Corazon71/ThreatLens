import os
import sys
import json

from dotenv import load_dotenv

import certifi
import pandas as pd
import numpy as np
import pymongo

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

MONGODB_URL = os.getenv("MONGODB_URL")
CA = certifi.where()

class DataExtract():
  def __init__(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  def csv2json_converter(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  def pushing_Data2MongoDB():
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
    
  if __name__ == "__main__":
    pass
    