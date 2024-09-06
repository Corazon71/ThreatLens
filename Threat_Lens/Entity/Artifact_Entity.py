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
class TLModelTrainArtifact:
  TrainedModelFPath : str
  TrainMetricArtifact : ClassificationArtifact
  TestMetricArtifact : ClassificationArtifact

@dataclass
class TLModelEvalArtifact:
  pass

@dataclass
class TLModelPushArtifact:
  pass
@dataclass
class TLClassficationMetricArtifact:
  pass