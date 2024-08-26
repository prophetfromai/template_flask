# app/__init__.py

from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)

    # Initialize Flask-RESTX
    api = Api(app, version='1.0', title='My API',
              description='A simple demonstration API')

    # Import routes and register them with the API
    with app.app_context():
        from . import routes
        # Assume routes are using Flask-RESTX's namespaces or resources
        api.add_namespace(routes.api)  # Assuming 'api' is defined in routes.py

    return app
