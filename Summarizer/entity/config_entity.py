import os, sys
from dataclasses import dataclass
from datetime import datetime
from from_root import from_root

from Summarizer.constants import *

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = SOURCE_DIR_NAME
    artifact_dir: str = os.path.join(ARTIFACTS_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    bucket_name: str = BUCKET_NAME
    file_name: str = FILE_NAME
    data_ingestion_artifacts: str = os.path.join(from_root(), training_pipeline_config.artifact_dir, DATA_INGESTION_ARTIFACTS_DIR)
    raw_data_dir: str = os.path.join(from_root(), data_ingestion_artifacts, RAW_DATA_DIR_NAME)
    train_file_path: str = os.path.join(data_ingestion_artifacts, DATA_INGESTION_TRAIN_DIR, TRAIN_FILE_NAME)
    test_file_path: str = os.path.join(data_ingestion_artifacts, DATA_INGESTION_TEST_DIR, TEST_FILE_NAME)


    