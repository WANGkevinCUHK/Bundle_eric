from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.now)



class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venue = db.Column(db.String(20), nullable=False)
    startTime = db.Column(db.DateTime, default=datetime.now)
    description = db.Column(db.String(100), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.now)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    creator = db.relationship("User", backref="createList")


class EventParticipant(db.Model):
    __tablename__ = "event_participants"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), primary_key=True)
    users = db.relationship("User", backref="eventList")
    events = db.relationship("Event", backref="participantList")

class Friendship(db.Model):
    __tablename__ = "friendship"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dst =  db.Column(db.Integer, nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.now)
    src_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    src = db.relationship("User", backref="friendList")