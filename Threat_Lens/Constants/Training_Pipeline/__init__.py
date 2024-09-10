import os
import sys
import pandas as pd
import numpy as np

# Common Constants
TARGET_COLUMN = "Result"
PIPELINE_NAME : str = "ThreatLens"
ARTIFACT_DIR : str = "Artifacts"
FILE_NAME : str = "Data.csv"

TRAIN_FILE_NAME : str = "Train.csv"
TEST_FILE_NAME : str = "Test.csv"

PREPROCESSING_OBJ_FILE_NAME = "Preprocessing.pkl"
MODEL_FILE_NAME = "Model.pkl"
SCHEMA_FILE_PATH = os.path.join("Data_Schema", "Schema.yaml")
SCHEMA_DROP_COLUMNS = "Drop_Clmn"
SAVED_MODEL_DIR = os.path.join("Saved_Models")

# Data Ingestion Constants
DATA_INGESTION_COLLECTION_NAME : str = "TLData"
DATA_INGESTION_DATABASE_NAME : str = "PunkRecords"
DATA_INGESTION_DIR_NAME : str = "Data_Ingestion"
DATA_INGESTION_FEATURESTORE_DIR_NAME : str = "Feature_Store"
DATA_INGESTION_INGESTED_DIR_NAME : str = "Ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2

# Data Validation Constants
DATA_VALIDATION_DIR_NAME : str = "Data_Validation"
DATA_VALIDATION_VALID_DIR : str = "ValidData"
DATA_VALIDATION_INVALID_DIR : str = "InvalidData"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "DriftReport"
DATA_VALIDATION_DRIFT_REPORT_NAME : str = "Report.yaml"

# Data Transformation Constants
DATA_TRANSFORMATION_DIR_NAME : str = "Data_Transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME : str = "Transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR : str = "Transformed_Object"
DATA_TRANSFORMATION_IMPUTER_PARAMS : dict = {
  "missing_values" : np.nan,
  "n_neighbors" : 3,
  "weights" : "uniform"
}
DATA_TRANSFORMATION_TRAIN_FILEPATH : str = "Train.npy"
DATA_TRANSFORMATION_TEST_FILEPATH : str = "Test.npy"

# Model Training Constants
MODEL_TRAINER_DIR_NAME : str = "Model_Trainer"
MODEL_TRAINER_TRAINED_DIR_NAME : str = "Trained_Model"
MODEL_TRAINER_TRAINED_MODEL_NAME : str = "Model.pkl"
MODEL_TRAINER_EXPECTED_SCORE : float = 0.6
MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD : float = 0.05

# Model Evaluation Constants
MODEL_EVALUATION_DIR_NAME : str = "Model_Evaluation"
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE : float = 0.02
MODEL_EVALUATION_REPORT_NAME : str = "report.yaml"

# Model Pusher Constants
MODEL_PUSHER_DIR_NAME : str = "Model Pusher"
MODEL_PUSHER_SAVED_MODEL_DIR = SAVED_MODEL_DIR
