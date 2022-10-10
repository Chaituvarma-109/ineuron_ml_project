import os.path
import sys
import json

import pandas as pd

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

from housing.Logger.log import logging
from housing.Exception.customexception import HousingException
from housing.Entity.config_entity import DatavalidationConfig
from housing.Entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact


class DataValidation:
    def __init__(self, data_valid_config: DatavalidationConfig, data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = data_valid_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_train_and_test_df(self) -> (str, str):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            return train_df, test_df
        except Exception as e:
            raise HousingException(e, sys) from e

    def is_train_test_file_exists(self) -> bool:
        try:
            logging.info(f"checking if training and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False

            # train and test file paths
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # checking whether train and test file paths exists
            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist
            logging.info(f"is training and test file exists? -> {is_available}")

            if not is_available:
                train_file_path = self.data_ingestion_artifact.train_file_path
                test_file_path = self.data_ingestion_artifact.test_file_path
                message = f"Training file: {train_file_path} or test file: {test_file_path} is not present."
                raise Exception(message)

            return is_available
        except Exception as e:
            raise HousingException(e, sys) from e

    def detect_outlier(self):
        pass

    def validate_dataset_schema(self) -> bool:
        try:
            validation_status = False

            # validate training and test dataset using schema file.
            # 1. Number of columns.
            # 2. check the values of "OCEAN PROXIMITY".
            # 3. check column names.

            validation_status = True

            return validation_status
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_and_save_data_drift_report(self) -> dict:
        try:
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df, test_df = self.get_train_and_test_df()

            profile.calculate(train_df, test_df)

            report = json.loads(profile.json())

            # create report directory
            report_file_path = self.data_validation_config.report_file_path
            report_dir_name = os.path.dirname(report_file_path)
            os.makedirs(report_dir_name, exist_ok=True)

            with open(report_file_path, 'w') as report_file:
                json.dump(report, report_file, indent=6)

            return report
        except Exception as e:
            raise HousingException(e, sys) from e

    def save_data_drift_report_page(self) -> None:
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df, test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df, test_df)

            # create dashboard page directory
            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir, exist_ok=True)

            dashboard.save(self.data_validation_config.report_page_file_path)
        except Exception as e:
            raise HousingException(e, sys) from e

    def is_data_drift_found(self) -> bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            return True
        except Exception as e:
            raise HousingException(e, sys) from e

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path= self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successfully."
            )
            logging.info(f"Data Validation Artifact: {data_validation_artifact}")

        except Exception as e:
            raise HousingException(e, sys) from e
