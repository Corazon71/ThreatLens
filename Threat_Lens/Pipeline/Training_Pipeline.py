import os
import sys

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

from Threat_Lens.Components.Data_Ingestion import TLDataIngest
from Threat_Lens.Components.Data_Transformation import TLDataTransform
from Threat_Lens.Components.Data_Validation import TLDataValid
from Threat_Lens.Components.Model_Evaluation import TLModelEval
from Threat_Lens.Components.Model_Pusher import TLModelPush
from Threat_Lens.Components.Model_Trainer import TLModelTrain

from Threat_Lens.Entity.Config_Entity import (
  TLTrainingPipelineConfig,
  TLDataIngestConfig,
  TLDataTransformConfig,
  TLDataValidConfig,
  TLModelEvalConfig,
  TLModelPushConfig,
  TLModelTrainConfig
)

from Threat_Lens.Entity.Artifact_Entity import (
  TLDataIngestArtifact,
  TLDataTransformArtifact,
  TLDataValidArtifact,
  TLModelEvalArtifact,
  TLModelPushArtifact,
  TLModelTrainArtifact
)

class TLTrainingPipeline():
  def __init__(self):
    pass

  def Start_Data_Ingest(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Data_Transform(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Data_Valid(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Model_Eval(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Model_Push(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Model_Train(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
  
  def Run_Pipeline(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)