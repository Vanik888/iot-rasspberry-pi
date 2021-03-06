import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


class BasicConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super secret'
    LOG_LEVEL = logging.DEBUG
