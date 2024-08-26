# app/__init__.py

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routes import router  # Import the router from routes.py


def create_app():
    # Create an instance of the FastAPI class
    app = FastAPI(
        title="My API",
        description="A simple demonstration API",
        version="1.0",
        docs_url="/docs",  # The URL for accessing Swagger UI
        openapi_url="/openapi.json"  # The URL for accessing the OpenAPI spec in JSON
    )

    # Redirect root URL to Swagger documentation or any other desired path
    # Exclude this endpoint from the OpenAPI schema
    @app.get("/", include_in_schema=False)
    async def root_redirect():
        return RedirectResponse(url="/docs")  # Redirect to /docs

    # Include the router from the routes module
    app.include_router(router, prefix="/api")

    return app
