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
  
def Save_numpy_array(FPath : str, Array : np.array):
  try:
    Dir_path = os.path.dirname(FPath)
    os.makedirs(Dir_path, exist_ok = True)
    with open(FPath, "wb") as FObj:
      np.save(FObj, Array)
  except Exception as e:
    raise TLException(e, sys)
  
def Load_numpy_array(FPath : str) -> np.array:
  try:
    with open(FPath, "rb") as FObj:
      return np.load(FObj)
  except Exception as e:
    raise TLException(e, sys)
  
def Save_object(FPath : str, Obj : object) -> None:
  try:
    logging.info("Entering the Save_object method of MainUtils class")
    os.makedirs(os.path.dirname(FPath), exist_ok = True)
    with open(FPath, "wb") as FObj:
      pickle.dump(Obj, FObj)
    logging.info("Exiting the Save_object method of MainUtils class")
  except Exception as e:
    raise TLException(e, sys)
  
def Load_object(FPath : str) -> object:
  try:
    if not os.path.exists(FPath):
      raise Exception(f"The file {FPath} not exist")
    with open(FPath, "rb") as FObj:
      print(FObj)
      return pickle.load(FObj)
  except Exception as e:
    raise TLException(e, sys)