# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:11:37 2019

@author: ritis
"""
import os

os.getcwd()
os.chdir(r'C:\Users\ritis\Documents\Jupyter Notebook Files\Flask\Large_Flask_Application_92_93_94')
from myproject import app
from myproject import db
from flask import render_template





@app.route(rule = '/')
def index():
    return render_template(template_name_or_list= 'home.html')


db.create_all()

if __name__ == '__main__':
    app.run(debug=True, use_reloader = False)
