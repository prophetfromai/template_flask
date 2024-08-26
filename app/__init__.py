# app/__init__.py

from flask import Flask, redirect, url_for
from flask_restx import Api


def create_app():
    app = Flask(__name__)

    # Initialize Flask-RESTX
    api = Api(
        app,
        version='1.0',
        title='My API',
        description='A simple demonstration API',
        doc='/docs',  # The URL for accessing Swagger UI
        prefix='/api'  # Prefix for all API endpoints
    )

    # Redirect root URL to Swagger documentation
    @app.route('/')
    def index():
        return redirect('/docs')  # Redirects to the Swagger UI

    # Import routes and register them with the API
    with app.app_context():
        from . import routes
        # Assuming 'api' is defined in routes.py
        api.add_namespace(routes.api)  # Registering the namespace with the API

    return app
