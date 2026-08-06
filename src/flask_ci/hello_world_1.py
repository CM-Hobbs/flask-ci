#!/usr/bin/env python3

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    '''
    Simple flask app to test flask is working NOW FROM THE CLI as a py app
    Doesnt need to run as flask like veriosn 0 (ie NO from src dir run: flask --app flask_app.hello_world run --debug)
    '''
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)