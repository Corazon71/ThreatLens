import os
import sys
import dill
import yaml
import pickle

import numpy as np

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

def Read_yaml_file(FPath : str) -> dict:
  try:
    with open(FPath, "rb") as yaml_file:
      return yaml.safe_load(yaml_file)
  except Exception as e:
    raise TLException(e, sys)
  
def Write_yaml_file(FPath : str, Content : object, replace : bool = False) -> None:
  try:
    if replace:
      if os.path.exists(FPath):
        os.remove(FPath)
    os.makedirs(os.path.dirname(FPath), exist_ok = True)
    with open(FPath, "w") as file:
      yaml.dump(Content, file)
  except Exception as e:
    raise TLException(e, sys)