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
    file_handler = RotatingFileHandler('logs/rasp.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

tools.init_board()

from app import routes
