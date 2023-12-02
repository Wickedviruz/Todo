from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/todo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    Secret_Key = os.getenv('SECRET_KEY')
