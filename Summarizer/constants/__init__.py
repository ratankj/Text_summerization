import os

ARTIFACTS_DIR: str = "artifacts"
SOURCE_DIR_NAME: str = 'Summarizer'

BUCKET_NAME: str = "news_data"
FILE_NAME: str = "news_summary.csv"
S3_BUCKET_DATA_URI = "s3://news-data/raw_data/"

# common files
METADATA_DIR = "metadata"
METADATA_FILE_NAME: str = "metadata.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# constants related to data ingestion
DATA_INGESTION_ARTIFACTS_DIR: str = "data_ingestion_artifacts"
RAW_DATA_DIR_NAME: str = "raw_data"
DATA_INGESTION_TRAIN_DIR: str = "train"
DATA_INGESTION_TEST_DIR: str = "test"