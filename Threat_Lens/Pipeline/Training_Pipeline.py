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
    self.TPConfig = TLTrainingPipelineConfig()

  def Start_Data_Ingest(self):
    try:
      self.DIConfig = TLDataIngestConfig(TPConfig = self.TPConfig)
      logging.info("Initiating Data Ingestion")
      DI = TLDataIngest(DIConfig = self.DIConfig)
      DI_Artifact = DI.initiate_DataIngestion()
      logging.info(f"Data Ingestion Completed Successfully - {DI_Artifact}")

      return DI_Artifact
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Data_Valid(self, PreArtifact: TLDataIngestArtifact):
    try:
      DVConfig = TLDataValidConfig(TPConfig = self.TPConfig)
      logging.info("Initiating Data Validation")
      DV = TLDataValid(DVConfig = DVConfig, DIArtifact = PreArtifact)
      DV_Artifact = DV.initiate_DataValidation()
      logging.info(f"Data Validation Completed Successfully - {DV_Artifact}")

      return DV_Artifact
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Data_Transform(self):
    try:
      pass
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Model_Train(self):
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
   
  def Run_Pipeline(self):
    try:
      DI_Artifact = self.Start_Data_Ingest()
      print(DI_Artifact)
      DV_Artifact = self.Start_Data_Valid(PreArtifact = DI_Artifact)
      print(DV_Artifact)
    except Exception as e:
      raise TLException(e, sys)