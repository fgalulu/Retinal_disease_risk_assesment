import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv('OAUTHLIB_INSECURE_TRANSPORT')
