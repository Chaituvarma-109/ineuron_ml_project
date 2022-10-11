from housing.Pipeline.pipeline import Pipeline
from housing.Exception.customexception import HousingException
from housing.Config.configuration import Configuration
from housing.Logger.log import logging


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)
    except Exception as e:
        logging.error(e)
        print(e)


if __name__ == "__main__":
    main()
