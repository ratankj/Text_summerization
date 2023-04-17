from Summarizer.components.data_ingestion import DataIngestion
from Summarizer.entity.config_entity import DataIngestionConfig

data_ingestion = DataIngestion(DataIngestionConfig())

data_ingestion_artifact = data_ingestion.initiate_data_ingestion()