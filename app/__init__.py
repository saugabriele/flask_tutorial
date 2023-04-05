from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import connect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine(app)

from app.routes import *
