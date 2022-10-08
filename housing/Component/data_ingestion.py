import sys

from housing.Exception.customexception import HousingException
from housing.Entity.config_entity import DataIngestionConfig
from housing.Logger.log import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
            pass
        except Exception as e:
            raise HousingException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
