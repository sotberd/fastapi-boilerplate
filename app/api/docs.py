"""OpenAPI documentation for the API v1."""

from app.core.config import settings

summary = f"""

{settings.APP_NAME} is a RESTful API that provides a minimal and clean structure for building FastAPI applications. This boilerplate includes essential tools and configurations to help you get started quickly with API development, following best practices and standard conventions.

"""

description = f"""

# Introduction

### Welcome to the API reference!

This reference provides a detailed explanation of all resources accessible through the `{settings.APP_NAME}` boilerplate project.
Our API is designed around REST principles, featuring predictable, resource-oriented URLs, and standard HTTP verbs and status codes, making it easy to extend and customize for any application.

### Versioning
The API base URL contains a version identifier. The current version is v1.
**New features, properties, and data models are continuously added, but the API will remain backwards compatible until deprecated.**

### Message Formats
Requests and responses are handled in JSON format, or in some cases, form-encoded data. All string properties are encoded using UTF-8.

### Extending the API
The structure provided by this boilerplate is designed for scalability, allowing you to easily extend functionality and add new endpoints, authentication mechanisms, and error handling as your project grows.

"""



tags_metadata = [
    {
        "name": "Health",
        "description": "Health endpoints are used for checking the status of the service",
    },
]

components_schemas = [
    {
        "component": "ValidationError",
        "schema": {
            "title": "ValidationError",
            "type": "object",
            "properties": {
                "error": {"title": "Error Message", "type": "string"},
                "status_code": {"title": "Status code", "type": "integer"},
            },
            "example": {
                "error": "Validation Error",
                "status_code": 422,
            },
        },
    },
    {
        "component": "HTTPValidationError",
        "schema": {
            "title": "HTTPValidationError",
            "type": "object",
            "properties": {
                "error": {"title": "Error Message", "type": "string"},
                "status_code": {"title": "Status code", "type": "integer"},
            },
            "example": {
                "error": "Validation Error",
                "status_code": 422,
            },
        },
    },
]
