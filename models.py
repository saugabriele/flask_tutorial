from flask_login import UserMixin

from app import db, logic_manager


@logic_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

class User(db.Document, UserMixin):
    meta = {'collection': 'users'}
    username = db.StringField()
    email = db.StringField(max_length=30)
    password = db.StringField()
