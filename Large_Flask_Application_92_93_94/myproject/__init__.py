# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:27:16 2019

@author: ritis
"""

import os

os.getcwd()
os.chdir(r'C:\Users\ritis\Documents\Jupyter Notebook Files\Flask\Large_Flask_Application_92_93_94')
os.getcwd()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(import_name= __name__, static_folder= 'static', template_folder= 'templates')
app.config['SECRET_KEY'] = 'mysecretkey'

base_dir = os.path.abspath(path = os.path.dirname(p = '__file__'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir,'data_consolidated.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app = app)

from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(blueprint=puppies_blueprint, url_prefix='/puppies')
app.register_blueprint(blueprint=owners_blueprint, url_prefix='/owners')