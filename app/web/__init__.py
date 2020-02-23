import os
import logging
import configparser
from src.main.flask_routes import Routes
from flask_cors import CORS
from flask import Flask

if os.getenv('FLASK_ENV') == 'development':
    from dotenv import load_dotenv

    load_dotenv(verbose=True)

log_filename = os.getenv('LOG_PATH')
log_level = os.getenv('LOG_LEVEL')

logging.basicConfig(
    filename=log_filename if not None else 'log.log',
    level=log_level if not None else logging.INFO
)

logging.warning('Starting application')


def create_app(config_test):
    app = Flask(__name__, instance_relative_config=True)

    config = configparser.ConfigParser()
    config.read('config.ini')

    app.config.from_mapping(
        SECRET_KEY=os.getenv("AWS")
    )

    if config is not None:
        app.config.update(config)

    if config_test is not None:
        app.config.update(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    CORS(app)

    Routes(app)

    return app
