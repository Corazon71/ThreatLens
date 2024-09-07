import os
import sys

from xgboost import XGBClassifier
from Threat_Lens.Exception.Exception import TLException
from Threat_Lens.Logger.Logger import logging

from Threat_Lens.Entity.Artifact_Entity import TLDataTransformArtifact, TLModelTrainArtifact
from Threat_Lens.Entity.Config_Entity import TLModelTrainConfig

from Threat_Lens.Utils.ML_Utils.Metrics.Classification_Metrics import get_classification_score
from Threat_Lens.Utils.ML_Utils.Model.Estimator import TLModel
from Threat_Lens.Utils.Main_Utils.Utils import Save_object, Load_object
from Threat_Lens.Utils.Main_Utils.Utils import Load_numpy_array

class TLModelTrain:
  def __init__(self, MTConfig : TLModelTrainConfig, DTArtifact : TLDataTransformArtifact):
    try:
      self.ModelTrainConfig = MTConfig
      self.DataTransformArtifact = DTArtifact
    except Exception as e:
      raise TLException(e, sys)

  def perform_Hyperparam_Tuning():
    pass
  
  def train_Model(self, X_trn, y_trn):
    try:
      Clsfr = XGBClassifier()
      Clsfr.fit(X_trn, y_trn)
      return Clsfr
    except Exception as e:
      raise TLException(e, sys)

  def initiate_ModelTrainer(self) -> TLModelTrainArtifact:
    try:
      TrFPath = self.DataTransformArtifact.TrnsfTrainFPath
      TsFPath = self.DataTransformArtifact.TrnsfTestFPath

      TrArray = Load_numpy_array(TrFPath)
      TsArray = Load_numpy_array(TsFPath)

      X_trn, y_trn, X_tst, y_tst = (
        TrArray[:, :-1],
        TrArray[:, -1],
        TsArray[:, :-1],
        TsArray[:, -1]
      )

      Model = self.train_Model(X_trn, y_trn)
      y_trn_pred = Model.predict(X_trn)
      clsf_trn_metric = get_classification_score(y_tru = y_trn, y_pred = y_trn_pred)

      if clsf_trn_metric.F1_Scr <= self.ModelTrainConfig.ExpctedAcc:
        print("Trained Model couldn't achieve expected accuracy")

      y_tst_pred = Model.predict(X_tst)
      clsf_tst_metric = get_classification_score(y_tru = y_tst, y_pred = y_tst_pred)

      diff = abs(clsf_trn_metric.F1_Scr - clsf_tst_metric.F1_Scr)

      if diff > self.ModelTrainConfig.OvrftUndrftThre:
        raise Exception("Model is not good enough to perform well")
      
      Preprocessor = Load_object(FPath = self.DataTransformArtifact.TrnsfObjFPath)
      ModelDirPath = os.path.dirname(self.ModelTrainConfig.ModelTrainDir)
      os.makedirs(ModelDirPath, exist_ok = True)
      TL_Model = TLModel(Preprocessor, Model)
      Save_object(FPath = self.ModelTrainConfig.TrainedModelPath, Obj = TL_Model)

      ModelTrainArtifact = TLModelTrainArtifact(
        TrainedModelFPath = self.ModelTrainConfig.TrainedModelPath,
        TrainMetricArtifact = clsf_trn_metric,
        TestMetricArtifact = clsf_tst_metric   
        )
      
      logging.info(f"Model Trainer Artifact : {ModelTrainArtifact}")

      return ModelTrainArtifact
    except Exception as e:
      raise TLException(e, sys)