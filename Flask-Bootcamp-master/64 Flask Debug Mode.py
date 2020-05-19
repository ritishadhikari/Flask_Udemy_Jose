# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:18:11 2019

@author: ritis
"""

from flask import Flask

app = Flask(import_name = __name__)


@app.route(rule = '/some_page/<name>')
def appname(name):
    return f"<h3> This is a page for : {name.title()} </h3>"

if __name__ == '__main__':
    app.run(debug=True)
