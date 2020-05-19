# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:56:40 2019

@author: ritis
"""

from flask import Flask

app = Flask(import_name= __name__)

@app.route(rule = '/puppy/<name>')
def puppy(name):
    return (f"100th letter : {name}")

if __name__ == '__main__':
    app.run(debug=True)
