from os import enviorn, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, '.env'))


class Config:
    FLASK_APP = enviorn.get('FLASK_APP')
    PORT = enviorn.get('PORT')

    # Database
    SQLALCHEMY_DATABASE_URI = enviorn.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_BINDS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
