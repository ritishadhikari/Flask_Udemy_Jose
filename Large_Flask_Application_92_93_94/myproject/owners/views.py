# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:30:46 2019

@author: ritis
"""

import os
os.chdir(r'C:\Users\ritis\Documents\Jupyter Notebook Files\Flask\Large_Flask_Application_92_93_94')

from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner_Project
from myproject.owners.forms import Addform

owners_blueprint = Blueprint(name = 'owners', import_name= __name__, template_folder= 'templates/owners')

@owners_blueprint.route(rule = '/add', methods = ['GET', 'POST'])
def add_owner():
    form = Addform()
    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner_Project(name = name, puppy_id = puppy_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(location=url_for(endpoint = 'puppies.list_pup'))
    return render_template(template_name_or_list='add_owners.html', form = form)
