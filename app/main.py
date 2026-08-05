import os
from flask import Flask, jsonify

app = Flask(__name__)

# Look for a env variable BUILD_SHA, if not found set to "dev"
BUILD_SHA = os.getenv("BUILD_SHA", "dev")

def normalise(name:str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be of type str")
    cleaned = join(name.split()).lower()
    if not cleaned:
        raise ValueError("name must not be empty")
    return cleaned

@app.get("/healthz")
def healthz():
    return jsonify(status="ok", build=BUILD_SHA)

@app.get("/greet/<name>")

