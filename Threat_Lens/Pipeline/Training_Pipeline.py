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
  
  def Start_Data_Transform(self, PreArtifact : TLDataValidArtifact):
    try:
      DTConfig = TLDataTransformConfig(TPConfig = self.TPConfig)
      logging.info("Initiating Data Transformation")
      DT = TLDataTransform(DTConfig = DTConfig, DVArtifact = PreArtifact)
      DT_Artifact = DT.initiate_DataTransformation()
      logging.info(f"Data Transformation Completed Successfully - {DT_Artifact}")

      return DT_Artifact 
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Model_Train(self, PreArtifact : TLDataTransformArtifact) -> TLModelTrainArtifact:
    try:
      MTConfig = TLModelTrainConfig(TPConfig = self.TPConfig)
      logging.info("Initiating Model Training")
      MT = TLModelTrain(MTConfig = MTConfig, DTArtifact = PreArtifact)
      MT_Artifact = MT.initiate_ModelTrainer()      
      logging.info(f"Model Training Completed Successfully - {MT_Artifact}")

      return MT_Artifact
    except Exception as e:
      raise TLException(e, sys)
 
  def Start_Model_Eval(self, PreArtifact : TLModelTrainArtifact, ValArtifact : TLDataValidArtifact) -> TLModelEvalArtifact:
    try:
      MEConfig = TLModelEvalConfig(TPConfig = self.TPConfig)
      logging.info("Initiated Model Evaluation")
      ME = TLModelEval(MEConfig = MEConfig, MTArtifact = PreArtifact, DVArtifact = ValArtifact)
      ME_Artifact = ME.initiate_ModelEvaluation()
      logging.info(f"Model Evaluation Completed Successfully - {ME_Artifact}")

      return ME_Artifact
    except Exception as e:
      raise TLException(e, sys)
  
  def Start_Model_Push(self, PreArtifact : TLModelEvalArtifact) -> TLModelPushArtifact:
    try:
      MPConfig = TLModelPushConfig(TPConfig = self.TPConfig)
      logging.info("Initiated Model Pusher")
      MP = TLModelPush(MPConfig = MPConfig, MEArtifact = PreArtifact)
      MP_Artifact = MP.initiate_ModelPusher()
      logging.info(f"Model Pushing Completed Successfully - {MP_Artifact}")

      return MP_Artifact
    except Exception as e:
      raise TLException(e, sys)
   
  def Run_Pipeline(self):
    try:
      DI_Artifact = self.Start_Data_Ingest()
      # print(DI_Artifact)
      DV_Artifact = self.Start_Data_Valid(PreArtifact = DI_Artifact)
      # print(DV_Artifact)
      DT_Artifact = self.Start_Data_Transform(PreArtifact = DV_Artifact)
      # print(DT_Artifact)
      MT_Artifact = self.Start_Model_Train(PreArtifact = DT_Artifact)
      # print(MT_Artifact)
      ME_Artifact = self.Start_Model_Eval(PreArtifact = MT_Artifact, ValArtifact = DV_Artifact)
      # print(ME_Artifact)
      MP_Artifact = self.Start_Model_Push(PreArtifact = ME_Artifact)
      print(ME_Artifact)
    except Exception as e:
      raise TLException(e, sys)