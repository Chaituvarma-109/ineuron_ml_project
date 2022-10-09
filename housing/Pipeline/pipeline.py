import sys

from housing.Config.configuration import Configuration
from housing.Logger.log import logging
from housing.Exception.customexception import HousingException
from housing.Entity.config_entity import DataIngestionConfig
from housing.Entity.artifact_entity import DataIngestionArtifact
from housing.Component.data_ingestion import DataIngestion


class Pipeline:
    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())

            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e
