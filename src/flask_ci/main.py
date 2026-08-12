#!/usr/bin/env python3

import os
from flask import Flask, jsonify

# get the Build SHA or return dev if none
BUILD_SHA = os.getenv("BUILD_SHA","dev")

app = Flask(__name__)


def normalise(name:str) -> str:
    '''Lower case and correct spacing'''
    if not isinstance(name, str):
        raise TypeError("name must be type str")
    #cleaned = " ".join(name.split()).lower()
    cleaned = " ".join(name.split()).upper()
    if not cleaned:
        raise ValueError("name must not be empty")
    return cleaned

@app.get("/healthz") # app.get automatically creates a http HEAD and OPTIONS for you
def healthz():
    '''my http health resource'''
    return jsonify(status="ok", build=BUILD_SHA)

@app.get("/greet/<name>")
def greet(name):
    '''basic page to say hello, creates resource /gree/<name>'''
    try:
        return jsonify(greeting=f"hello {normalise(name)}",timmy="awesome")
    except ValueError as e:
        return jsonify(error=str(e)),400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=60000)

