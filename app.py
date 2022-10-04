import sys
from flask import Flask

from housing.Logger.log import logging
from housing.Exception.customexception import HousingException

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are raising custom exception.")
    except Exception as e:
        house = HousingException(e, sys)
        logging.info(house.error_message)
        logging.info("we are testing module")
    return 'Starting Machine Learning Project'


if __name__ == "__main__":
    app.run(debug=True)
