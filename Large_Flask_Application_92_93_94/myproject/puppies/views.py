# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:31:36 2019

@author: ritis
"""
import os
os.chdir(r'C:\Users\ritis\Documents\Jupyter Notebook Files\Flask\Large_Flask_Application_92_93_94')


from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.puppies.forms import Addform, DelForm
from myproject.models import Puppy_Project

puppies_blueprint = Blueprint(name = 'puppies', import_name = __name__, template_folder= 'templates/puppies')



@puppies_blueprint.route(rule = '/add', methods =['GET','POST'])
def add_puppy():
    form = Addform()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy_Project(name = name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(location = url_for(endpoint = 'puppies.list_pup'))
    return render_template(template_name_or_list = 'add.html', form = form)

@puppies_blueprint.route(rule = '/delete', methods = ['GET','POST'])
def del_puppy():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        del_id = Puppy_Project.query.get(ident=id)
        db.session.delete(del_id)
        db.session.commit()
        return redirect(location=url_for(endpoint = 'puppies.list_pup'))
    return render_template(template_name_or_list= 'delete.html', form = form)

@puppies_blueprint.route(rule = '/list_puppies')
def list_pup():
    pups = Puppy_Project.query.all()
    return render_template(template_name_or_list='list.html', pups = pups)
