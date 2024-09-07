from dataclasses import dataclass

@dataclass
class TLDataIngestArtifact:
  TrainFPath : str
  TestFPath : str

@dataclass
class TLDataValidArtifact:
  ValStatus : bool
  ValTrainFPath : str
  ValTestFPath : str
  InvalTrainFPath : str
  InvalTestFPath : str
  DriftReportFPath : str

@dataclass
class TLDataTransformArtifact:
  TrnsfObjFPath : str
  TrnsfTrainFPath : str
  TrnsfTestFPath : str

@dataclass
class TLClassificationMetricArtifact:
  F1_Scr : float
  Precision_Scr : float
  Recall_Scr : float
  pass

@dataclass
class TLModelTrainArtifact:
  TrainedModelFPath : str
  TrainMetricArtifact : TLClassificationMetricArtifact
  TestMetricArtifact : TLClassificationMetricArtifact

@dataclass
class TLModelEvalArtifact:
  pass

@dataclass
class TLModelPushArtifact:
  pass