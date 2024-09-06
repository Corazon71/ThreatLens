import os
import sys

from sklearn.metrics import f1_score, precision_score, recall_score
from Threat_Lens.Entity.Artifact_Entity import ClassificationMetricArtifact
from Threat_Lens.Exception.Exception import TLException

def get_classification_score(y_tru, y_pred) -> ClassificationMetricArtifact:
  try:
    Model_F1_Score = f1_score(y_tru, y_pred)
    Model_Recall_Score = recall_score(y_tru, y_pred)
    Model_Precision_Score = precision_score(y_tru, y_pred)
    Clss_Metric = ClassificationMetricArtifact(F1_Scr = Model_F1_Score, Recall_Scr = Model_Recall_Score, Precision_Scr = Model_Precision_Score)
  except Exception as e:
    raise TLException(e, sys)