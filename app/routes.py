# app/routes.py

import os
from flask import jsonify, request, current_app as app

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route("/json")
def hello_json():
    """Return a JSON response."""
    return jsonify(message="Hello, World!", status="success")

@app.route("/greet/<name>")
def greet(name):
    """Greet the user by name."""
    return f"Hello, {name.capitalize()}!"

@app.route("/calculate", methods=["POST"])
def calculate():
    """Perform a simple addition operation with JSON input."""
    data = request.get_json()
    try:
        x = data["x"]
        y = data["y"]
        result = x + y
        return jsonify(result=result, status="success")
    except (KeyError, TypeError):
        return jsonify(message="Invalid input. Please provide 'x' and 'y' in the request body.", status="error"), 400

@app.route("/repeat", methods=["GET", "POST"])
def repeat():
    """Repeat a phrase or word provided in the query parameter."""
    if request.method == "GET":
        phrase = request.args.get("phrase", "Hello")
        count = int(request.args.get("count", 1))
    else:
        data = request.get_json()
        phrase = data.get("phrase", "Hello")
        count = int(data.get("count", 1))
    
    return f"{phrase} " * count
