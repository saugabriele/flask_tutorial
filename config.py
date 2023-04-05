import os
from mongoengine import connect, disconnect


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "kkkkkkey!!"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGODB_USERNAME = "biggabriel2531"
    MONGODB_PASSWORD = "Conforama"
    MONGODB_CONNECT = True
    MONGODB_DB = "my_app_db"
