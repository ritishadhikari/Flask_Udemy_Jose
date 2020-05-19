import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.dirname(p = os.path.realpath(path = '__file__'))

app = Flask(import_name= __name__, static_folder= 'static', template_folder= 'templates')

# Setting up SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#creating the object of the SQL Alchemy by feeding the flask app
db = SQLAlchemy(app = app)

Migrate(app,db)

class Puppy(db.Model):

    #Manual Table Name Choice
    __tablename__ = 'puppies'

    #set up the columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


    def __repr__(self):
        return f"{self.name} is {self.age} year\'s old"
