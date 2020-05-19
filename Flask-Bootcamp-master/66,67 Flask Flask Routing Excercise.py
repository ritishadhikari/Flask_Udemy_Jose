# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 01:31:06 2019

@author: ritis
"""

from flask import Flask

app = Flask(import_name= __name__)

@app.route(rule='/')
def intro():
    return 'My Name is Ritish'

@app.route(rule = '/puppy_latin/<name>')
def puppy_name(name):
    if name[-1] == 'y':
        name_new = name[:-1] + 'iful'
        return (f"<h1> Name of the {name} latin Puppy is : {name_new} </h1>")
    else:
        name_new = name + 'y'
        return (f"<h1> Name of the {name} latin Puppy is : {name_new} </h1>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, use_debugger=True)
