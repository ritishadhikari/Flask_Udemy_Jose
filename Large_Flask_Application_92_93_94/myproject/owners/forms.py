# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:30:19 2019

@author: ritis
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class Addform(FlaskForm):
    name = StringField("Name of Owner")
    puppy_id = IntegerField("Puppy ID:")
    submit = SubmitField("Add owner")
