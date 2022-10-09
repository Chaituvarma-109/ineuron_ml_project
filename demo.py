from housing.Pipeline.pipeline import Pipeline
from housing.Exception.customexception import HousingException
from housing.Logger.log import logging


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(e)
        print(e)


if __name__ == "__main__":
    main()
