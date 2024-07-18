from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    followers = db.relationship(
        'User',
        secondary='follows',
        primaryjoin='User.id == follows.c.followed_id',
        secondaryjoin='User.id == follows.c.follower_id',
        backref=db.backref('following', lazy='dynamic'),
        lazy='dynamic'
    )

class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class FollowerCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date, default=datetime.utcnow)
    count = db.Column(db.Integer)

    user = db.relationship('User', backref=db.backref('follower_counts', lazy='dynamic'))
