# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:29:05 2019

@author: ritis
"""

from flask import Flask, render_template

app = Flask(import_name= __name__)

#app.config.update({'TEMPLATES_AUTO_RELOAD': True})

@app.route(rule = '/')
def index():
    return render_template('Flask_Basic_Template_68.html')


if __name__ == '__main__':
    app.run(debug=True)
