import os
import sys

import pandas as pd

from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

from Threat_Lens.Entity.Artifact_Entity import TLDataValidArtifact, TLModelTrainArtifact, TLModelEvalArtifact
from Threat_Lens.Entity.Config_Entity import TLModelEvalConfig

from Threat_Lens.Utils.Main_Utils.Utils import Save_object, Load_object, Write_yaml_file
from Threat_Lens.Utils.ML_Utils.Metrics.Classification_Metrics import get_classification_score
from Threat_Lens.Utils.ML_Utils.Model.Estimator import TLModel
from Threat_Lens.Utils.ML_Utils.Model.Estimator import ModelResolver

from Threat_Lens.Constants.Training_Pipeline import TARGET_COLUMN

class TLModelEval:
  def __init__(self, MEConfig : TLModelEvalConfig, MTArtifact : TLModelTrainArtifact, DVArtifact : TLDataValidArtifact):
    try:
      self.ModelEvalConfig = MEConfig
      self.ModelTrainArtifact = MTArtifact
      self.DataValidArtifact = DVArtifact
    except Exception as e:
      raise TLException(e, sys)
    
  def initiate_ModelEvaluation(self) -> TLModelEvalArtifact:
    try:
      ValTrPath = self.DataValidArtifact.ValTrainFPath
      ValTsPath = self.DataValidArtifact.ValTestFPath
      TrDF = pd.read_csv(ValTrPath)
      TsDF = pd.read_csv(ValTsPath)

      DF = pd.concat([TrDF, TsDF])
      yTru = DF[TARGET_COLUMN]
      yTru.replace(-1, 0, inplace = True)

      TrnModelFPath = self.ModelTrainArtifact.TrainedModelFPath

      ModelRslvr = ModelResolver()
      AccptModel = True

      if not ModelRslvr.is_model_exist():
        ModelEvalArtifact = TLModelEvalArtifact(
          IsModelAccpt = AccptModel,
          ImprovedAcc = None,
          BestModelPath = None,
          TrainedModelPath = TrnModelFPath,
          TrainModelMetricArtifact = self.ModelTrainArtifact.TestMetricArtifact,
          BestModelMetricArtifact = None
        )
        logging.info(f"New Model Evaluation Artifact{ModelEvalArtifact}")
        ModelEvalReport = ModelEvalArtifact.__dict__
        Write_yaml_file(self.ModelEvalConfig.ReportPath, ModelEvalReport)
        return ModelEvalArtifact
      
      Latest_ModelPath = ModelRslvr.get_best_model_path()
      Latest_Model = Load_object(Latest_ModelPath)
      Trn_Model = Load_object(TrnModelFPath)

      yTrn_pred = Trn_Model.predict(DF)
      yLatest_pred = Latest_Model.predict(DF)

      Trn_Metric = get_classification_score(yTru, yTrn_pred)
      Latest_Metric = get_classification_score(yTru, yLatest_pred)
      NewAcc = Trn_Metric.F1_Scr - Latest_Metric.F1_Scr

      if self.ModelEvalConfig.Thre < NewAcc:
        AccptModel = True

      else:
        AccptModel = False

      ModelEvalArtifact = TLModelEvalArtifact(
        IsModelAccpt = AccptModel,
        ImprovedAcc = NewAcc,
        BestModelPath = Latest_ModelPath,
        TrainedModelPath = TrnModelFPath,
        TrainModelMetricArtifact = Trn_Metric,
        BestModelMetricArtifact = Latest_Metric 
      )
      logging.info(f"Replaced Model Evaluation Artifact{ModelEvalArtifact}")
      ModelEvalReport = ModelEvalArtifact.__dict__
      Write_yaml_file(self.ModelEvalConfig.ReportPath, ModelEvalReport)
      
      return ModelEvalArtifact
    except Exception as e:
      raise TLException(e, sys)
