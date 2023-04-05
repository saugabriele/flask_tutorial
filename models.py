from app import db


class User(db.Document):
    meta = {'collection': 'users'}
    username = db.StringField()
    email = db.StringField(max_length=30)
    password = db.StringField()
