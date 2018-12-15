import os
import logging
from logging.handlers import RotatingFileHandler


from flask import Flask
from config import BasicConfig

import app.tools

app = Flask(__name__)
app.config.from_object(BasicConfig)

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    LOG_LEVEL = app.config.get('LOG_LEVEL') or logging.INFO
    file_handler = RotatingFileHandler('logs/rasp.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(LOG_LEVEL)

    app.logger.setLevel(LOG_LEVEL)
    app.logger.addHandler(file_handler)

tools.init_board()

from app import routes
