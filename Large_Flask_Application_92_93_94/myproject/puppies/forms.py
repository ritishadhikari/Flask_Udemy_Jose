# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:31:17 2019

@author: ritis
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class Addform(FlaskForm):
    name = StringField("Name of Puppy: ")
    submit = SubmitField("Add Puppy")
    

class DelForm(FlaskForm):
    id = IntegerField("Id Number of Puppy to Remove: ")
    submit = SubmitField("Remove Puppy")