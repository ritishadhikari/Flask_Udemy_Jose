# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:28:07 2019

@author: ritis
"""

import os

os.getcwd()
os.chdir(r'C:\Users\ritis\Documents\Jupyter Notebook Files\Flask\Large_Flask_Application_92_93_94')
os.getcwd()


from myproject import db


class Puppy_Project(db.Model):
    __tablename__ = 'puppie_project'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    #-----------------------------------------------#
    # one-one relationship with puppie and its owner
    #-----------------------------------------------#
    owner = db.relationship(argument = 'Owner_Project', backref='puppie', lazy = 'select', uselist = False)
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        if self.owner:
            return f"Puppie {self.name} has owner {self.owner.name}"
        else:
            return f"Puppie {self.name} has no owner"

class Owner_Project(db.Model):
    __tablename__ = 'owner_project'
    owner_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey(column = 'puppie_project.id'))
    
    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
        
    def __repr__(self):
        return f"Owner Name : {self.name}"