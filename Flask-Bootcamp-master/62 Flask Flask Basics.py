# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:57:14 2019

@author: ritis
"""

from flask import Flask

#creating an application object of an instance of class Flask.
#The __name__ variable thats being passed into Flask Class Call is set to the name of the module
app = Flask(import_name= __name__)

@app.route(rule = '/some_page/')
def index():
    return '<h1>Hello Puppy!</h1>'
    #return '<br>'
    #return '<p>This is a Paragraph on Puppy</p>'
    #return '<a href='https://www.google.com'>Explore Google</a>'

if __name__ == '__main__':
    app.run()
