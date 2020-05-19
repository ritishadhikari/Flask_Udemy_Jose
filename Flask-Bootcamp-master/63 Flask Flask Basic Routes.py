# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:08:07 2019

@author: ritis
"""

from flask import Flask

app = Flask(import_name= __name__)

@app.route(rule = "/information",   )
def info():
    return "<h2>Puppies are Cute </h2>"

if __name__ == '__main__':
    app.run()
