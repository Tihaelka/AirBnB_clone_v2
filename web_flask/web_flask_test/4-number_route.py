#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:42:23 2020

@author: Robinson Montes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Adding a specific route /hbnb"""
    return 'HBNB'
