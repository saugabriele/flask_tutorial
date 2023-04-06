import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "kkkkkkey!!"
    # database configuration
    MONGODB_SETTINGS = [
        {
            "db": "my_app_db",
            "host": "localhost",
            "port": 27017,
            "alias": "default",
        }
    ]
