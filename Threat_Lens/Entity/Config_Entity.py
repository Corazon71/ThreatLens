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
    self.FSFilePath : str = os.path.join(self.DataIngestDir, Training_Pipeline.DATA_INGESTION_FEATURESTORE_DIR_NAME, Training_Pipeline.FILE_NAME)
    self.TrainPath : str = os.path.join(self.DataIngestDir, Training_Pipeline.DATA_INGESTION_INGESTED_DIR_NAME, Training_Pipeline.TRAIN_FILE_NAME)
    self.TestPath : str = os.path.join(self.DataIngestDir, Training_Pipeline.DATA_INGESTION_INGESTED_DIR_NAME, Training_Pipeline.TEST_FILE_NAME)
    self.TTSRatio : float = Training_Pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    self.CllctnName : str = Training_Pipeline.DATA_INGESTION_COLLECTION_NAME
    self.DBName : str = Training_Pipeline.DATA_INGESTION_DATABASE_NAME

class TLDataValidConfig:
  def __init__(self, TPConfig : TLTrainingPipelineConfig):
    self.DataValidDir : str = os.path.join(TPConfig.ArtifactDir, Training_Pipeline.DATA_VALIDATION_DIR_NAME)
    self.ValidDataDir : str = os.path.join(self.DataValidDir, Training_Pipeline.DATA_VALIDATION_VALID_DIR)
    self.InvalidDataDir : str = os.path.join(self.DataValidDir, Training_Pipeline.DATA_VALIDATION_INVALID_DIR)
    self.ValidTrainPath : str = os.path.join(self.ValidDataDir, Training_Pipeline.TRAIN_FILE_NAME)
    self.ValidTestPath : str = os.path.join(self.ValidDataDir, Training_Pipeline.TEST_FILE_NAME)
    self.InvalidTrainPath : str = os.path.join(self.InvalidDataDir, Training_Pipeline.TRAIN_FILE_NAME)
    self.InvalidTestPath : str = os.path.join(self.InvalidDataDir, Training_Pipeline.TEST_FILE_NAME)
    self.DRFilePath : str = os.path.join(
      self.DataValidDir,
      Training_Pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
      Training_Pipeline.DATA_VALIDATION_DRIFT_REPORT_NAME,
    )
    
class TLDataTransformConfig:
  def __init__(self, TPConfig : TLTrainingPipelineConfig):
    self.DataTransformDir : str = os.path.join(TPConfig.ArtifactDir, Training_Pipeline.DATA_TRANSFORMATION_DIR_NAME)
    self.TrnsfTrainPath : str = os.path.join(self.DataTransformDir, Training_Pipeline.DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME, Training_Pipeline.TRAIN_FILE_NAME.replace("csv", "npy"))
    self.TrnsfTestPath : str = os.path.join(self.DataTransformDir, Training_Pipeline.DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME, Training_Pipeline.TEST_FILE_NAME.replace("csv", "npy"))
    self.TrnsfObjPath : str = os.path.join(self.DataTransformDir, Training_Pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR, Training_Pipeline.PREPROCESSING_OBJ_FILE_NAME)

class TLModelTrainConfig:
  def __init__(self, TPConfig : TLTrainingPipelineConfig):
    self.ModelTrainDir : str = os.path.join(TPConfig.ArtifactDir, Training_Pipeline.MODEL_TRAINER_DIR_NAME)
    self.TrainedModelPath : str = os.path.join(self.ModelTrainDir, Training_Pipeline.MODEL_TRAINER_TRAINED_DIR_NAME, Training_Pipeline.MODEL_FILE_NAME)
    self.ExpctedAcc : float = Training_Pipeline.MODEL_TRAINER_EXPECTED_SCORE
    self.OvrftUndrftThre : float = Training_Pipeline.MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD

class TLModelEvalConfig:
  def __init__(self):
    pass

class TLModelPushConfig:
  def __init__(self):
    pass