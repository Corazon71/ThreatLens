import os
import sys

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging
from Threat_Lens.Pipeline.Training_Pipeline import TLTrainingPipeline

def start_training():
  try:
    pass
  except Exception as e:
    raise TLException(e, sys)
  
if __name__ == "__main__":
  start_training()