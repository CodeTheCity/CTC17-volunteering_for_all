
from settings import *

import os
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "volunteer.db"))

        
# Web API

from flask import Flask
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

volunteer_skills = db.Table('volunteer_skills',
    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

volunteer_interest = db.Table("volunteer_interest",
    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

charity_category = db.Table('charity_category',
    db.Column('charity_id', db.Integer, db.ForeignKey('charity.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    bio = db.Column(db.Text)
    paused = db.Column(db.Boolean, default=False)
    skills = db.relationship('Skill', secondary=volunteer_skills, lazy='subquery',
                             backref=db.backref('volunteers', lazy=True))
    interested = db.relationship('Category', secondary=volunteer_interest, lazy='subquery',
                                 backref=db.backref('volunteers', lazy=True))
    
class Charity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    categories = db.relationship('Category', secondary=charity_category, lazy='subquery',
                                 backref=db.backref('charities', lazy=True))
    def __repr(self):
        return "<Charity: {}>".format(self.name)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    def __repr__(self):
        return "<Category: {}>".format(self.name)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    def __repr__(self):
        return "<Skill: {}>".format(self.name)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey("charity.id"), nullable=False)
    description = db.Column(db.Text)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Integer, db.ForeignKey("task.id"), nullable=False)
    volunteer = db.Column(db.Integer, db.ForeignKey("volunteer.id"), nullable=False)
    
from web import *

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
