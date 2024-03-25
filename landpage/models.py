from landpage.ext.database import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(140))