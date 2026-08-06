#!/usr/bin/env python3

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    '''
    Simple flask app to test flask is working
    from src dir run:
    flask --app flask_app.hello_world run --debug
    '''
    return "Hello World!"
