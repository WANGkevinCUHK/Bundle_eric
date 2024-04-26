from exts import db
from datetime import datetime



class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, nullable=False)
    venue = db.Column(db.String(20), nullable=False)
    startTime = db.Column(db.DateTime, default=datetime.now)
    description = db.Column(db.String(100), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.now)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.now)
    activity_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    activity = db.relationship("Event", backref="participants")


# class Friendship(db.Model):
#     __tablename__ = "friendship"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     created_time = db.Column(db.DateTime, default=datetime.now)