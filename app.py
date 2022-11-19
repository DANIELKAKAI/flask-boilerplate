import logging
import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config
from api.dispenser import api
from models.dispenser import db

from flask import Flask


migrate = Migrate()

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)
    migrate.init_app(app, db)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
