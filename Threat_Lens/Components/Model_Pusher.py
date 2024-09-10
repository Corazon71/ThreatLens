import os
import sys
import shutil

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

from Threat_Lens.Entity.Artifact_Entity import TLModelPushArtifact, TLModelEvalArtifact
from Threat_Lens.Entity.Config_Entity import TLModelPushConfig

from Threat_Lens.Utils.Main_Utils.Utils import Save_object, Load_object, Write_yaml_file
from Threat_Lens.Utils.ML_Utils.Metrics.Classification_Metrics import get_classification_score

class TLModelPush:
  def __init__(self, MPConfig : TLModelPushConfig, MEArtifact : TLModelEvalArtifact):
    try:
      self.ModelPushConfig = MPConfig
      self.ModelEvalArtifact = MEArtifact
    except Exception as e:
      raise TLException(e, sys)
    
  def initiate_ModelPusher(self) -> TLModelPushArtifact:
    try:
      TrnModelPath = self.ModelEvalArtifact.TrainedModelPath

      ModelFilePath = self.ModelPushConfig.ModelFilePath
      os.makedirs(os.path.dirname(ModelFilePath), exist_ok = True)
      shutil.copy(src = TrnModelPath, dst = ModelFilePath)

      SavedModelPath = self.ModelPushConfig.SavedModelPath
      os.makedirs(os.path.dirname(SavedModelPath), exist_ok = True)
      shutil.copy(src = TrnModelPath, dst = SavedModelPath)
    
      ModelPushArtifact = TLModelPushArtifact(
        SavedModelPath = SavedModelPath,
        ModelFilePath = ModelFilePath
      )

      return ModelPushArtifact
    except Exception as e:
      raise TLException(e, sys)