#!/usr/bin/env python
from app import db

relationship_table = db.Table('datacenter_server_relationship',
                              db.Column('datacenter_id', db.Integer, db.ForeignKey('datacenters.id'), nullable=False),
                              db.Column('server_id', db.Integer, db.ForeignKey('servers.id'), nullable=False),
                              db.PrimaryKeyConstraint('datacenter_id', 'server_id'))

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.username

class Datacenters(db.Model):
    __tablename__ = 'datacenters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),  index=True)
    location = db.Column(db.String(64))
    capacity = db.Column(db.Integer)
    tier = db.Column(db.Integer)
    servers = db.relationship('Servers', secondary=relationship_table, backref='datacenters')

class Servers(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    manufacturer = db.Column(db.String(64))
    model = db.Column(db.String(64))
    serial_number = db.Column(db.String(64))
    os = db.Column(db.String(64))
