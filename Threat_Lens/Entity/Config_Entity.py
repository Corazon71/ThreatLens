import os

from datetime import datetime

from Threat_Lens.Constants import Training_Pipeline

print(Training_Pipeline.PIPELINE_NAME)
print(Training_Pipeline.ARTIFACT_DIR)

class TLTrainingPipelineConfig:
  def __init__(self, TimeStamp = datetime.now()):
    TimeStamp = TimeStamp.strftime("%m_%d_%Y_%H_%M_%S")
    self.PipelineName = Training_Pipeline.PIPELINE_NAME
    self.ArtifactName = Training_Pipeline.ARTIFACT_DIR
    self.ArtifactDir = os.path.join(self.ArtifactName, TimeStamp)
    self.TimeStamp : str = TimeStamp

class TLDataIngestConfig:
  def __init__(self, TPConfig : TLTrainingPipelineConfig):
    self.DataIngestDir : str = os.path.join(TPConfig.ArtifactDir, Training_Pipeline.DATA_INGESTION_DIR_NAME)
    self.FS_FilePath : str = os.path.join(self.DataIngestDir, Training_Pipeline.DATA_INGESTION_FEATURESTORE_DIR_NAME, Training_Pipeline.FILE_NAME)
    self.TrainPath : str = os.path.join(self.DataIngestDir, Training_Pipeline.DATA_INGESTION_INGESTED_DIR_NAME, Training_Pipeline.TRAIN_FILE_NAME)
    self.TestPath : str = os.path.join(self.DataIngestDir, Training_Pipeline.DATA_INGESTION_INGESTED_DIR_NAME, Training_Pipeline.TEST_FILE_NAME)
    self.TTSRatio : float = Training_Pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    self.CllctnName : str = Training_Pipeline.DATA_INGESTION_COLLECTION_NAME
    self.DBName : str = Training_Pipeline.DATA_INGESTION_DATABASE_NAME

class TLDataValidConfig:
  def __init__(self):
    pass

class TLDataTransformConfig:
  def __init__(self):
    pass

class TLModelTrainConfig:
  def __init__(self):
    pass

class TLModelEvalConfig:
  def __init__(self):
    pass

class TLModelPushConfig:
  def __init__(self):
    pass