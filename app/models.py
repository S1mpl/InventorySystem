#!/usr/bin/env python
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    authenticated = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<User %r>' % self.username

class Datacenters(db.Model):
    __tablename__ = 'datacenters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),  index=True)
    location = db.Column(db.String(255))
    capacity = db.Column(db.Integer)
    tier = db.Column(db.Integer)
    servers = db.relationship('Servers', backref='server', lazy='dynamic')

class Servers(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    manufacturer = db.Column(db.String(64))
    model = db.Column(db.String(64))
    serial_number = db.Column(db.String(64))
    os = db.Column(db.String(64))
    datacenter_id = db.Column(db.Integer, db.ForeignKey('datacenters.id'))

@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(username=user_id).first()