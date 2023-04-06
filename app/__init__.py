from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
logic_manager = LoginManager(app)
db = MongoEngine(app)

from app.routes import *
