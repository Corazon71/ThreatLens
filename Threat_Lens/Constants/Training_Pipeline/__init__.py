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
DATA_VALIDATION_DIR_NAME : str = "DataValidation"
DATA_VALIDATION_VALID_DIR : str = "ValidData"
DATA_VALIDATION_INVALID_DIR : str = "InvalidData"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "DriftReport"
DATA_VALIDATION_DRIFT_REPORT_NAME : str = "Report.yaml"

# Data Transformation Constants

# Model Training Constants