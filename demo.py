import os

from housing.Pipeline.pipeline import Pipeline
from housing.Exception.customexception import HousingException
from housing.Config.configuration import Configuration
from housing.Logger.log import logging


def main():
    try:
        config_path = os.path.join("config", 'config.yaml')
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        # pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        # data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()
