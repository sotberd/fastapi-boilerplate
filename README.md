<p align="center">
    <img src="https://camo.githubusercontent.com/4ebb06d037b495f2c4c67e0ee4599f747e94e6323ece758a7da27fbbcb411250/68747470733a2f2f666173746170692e7469616e676f6c6f2e636f6d2f696d672f6c6f676f2d6d617267696e2f6c6f676f2d7465616c2e706e67" alt="fastapi-logo">
</p>
<p align="center">
  <a href="https://www.python.org/downloads/release/python-3110/" target="_blank">
      <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python 3.11">
  </a>
  <a href="https://github.com/sotberd/fastapi-boilerplate/actions/workflows/ci.yml?query=workflow%3ACI%3Amain" target="_blank">
    <img src="https://github.com/sotberd/fastapi-boilerplate/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI">
  </a>
</p>
<h1 align="center">FastAPI Boilerplate</h1>
<p align="center">
    <em><strong>FastAPI Boilerplate</strong> is a minimal template for creating FastAPI applications with a clean project structure and best practices.</em>
</p>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Local Development](#local-development)
  - [Running the API](#running-the-api)
  - [Testing](#testing)
  - [Code Quality](#code-quality)
- [Build and run](#build-and-run)
- [Environment Variables](#environment-variables)
- [License](#license)

## Overview

The FastAPI Boilerplate is a minimal and production-ready template for quickly setting up FastAPI applications. It provides a clean and organized project structure with best practices to help you get started with building APIs efficiently. This boilerplate includes:

- `Modular Structure:` Organized into clear directories for routes, schemas, core configurations, etc.
- `Environment Variables:` Easily configurable settings through environment variables, ensuring flexibility in various environments (development, staging, production).
- `Testing Support:` Built-in testing framework using pytest to ensure reliable and robust applications.
- `Pre-commit Hooks:` Automatic code formatting and linting before each commit to maintain code quality.
- `Docker Support:` Preconfigured Docker setup for containerized deployments, making it easier to deploy the app anywhere.
- `Extensibility:` The structure is designed to be easily extended with additional functionality, allowing developers to customize it for their specific needs.

Whether you're building a simple REST API or a complex microservice, this boilerplate serves as a solid foundation for your FastAPI projects.

## Getting Started

### Local Development

To set up the project locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/sotberd/fastapi-boilerplate.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the API

To start the API server, run:

```bash
fastapi dev --host 0.0.0.0 --port 8000
```

You can then use the following curl commands to interact with the API:

```bash
curl -X GET http://localhost:8000/api/v1/health
```

### Testing

Testing is crucial for maintaining the reliability of the API. This project uses `pytest` for testing.

```bash
./scripts/test.sh

open htmlcov/index.html
```

### Code Quality

To maintain code quality, this project uses pre-commit hooks. These hooks can automatically format and lint your code before commits.

1. Install pre-commit hooks:

   ```bash
   pre-commit install
   ```

2. Run pre-commit hooks:

   ```bash
   pre-commit run --all-files
   ```

3. Formatting:

   To automatically format your code, use the following script:

   ```bash
   ./scripts/format.sh
   ```

## Build and Run

This project uses Docker for containerization, simplifying deployment across various environments.

1. **Build the Docker image:**

   ```bash
   docker build -t fastapi-boilerplate .
   ```

2. Run the Docker container for the API:

   ```bash
   docker run -d -p 8000:8000 fastapi-boilerplate fastapi run --host 0.0.0.0 --port 8000
   ```

   > ℹ️ The API will be accessible at http://localhost:8000.

## Environment Variables

To configure the behavior of the API, you can use the following environment variables:

- `DEBUG:` Enable or disable debug mode. Default is `True`.
- `APP_NAME:` Name of the application. Default is `"FastAPI Boilerplate"`.
- `API_V1_STR:` API versioning string. Default is `"/api/v1"`.
- `DOCS_URL:` URL for the Swagger documentation. Default is `"/docs"`.
- `REDOC_URL:` URL for the ReDoc documentation. Default is `"/"`.
- `OPENAPI_JSON_PATH:` Path to the OpenAPI spec file. Default is `"./openapi.json"`.
- `VERSION:` API version. Default is `"1.0.0"`.
- `BACKEND_CORS_ORIGINS:` A JSON-formatted list of allowed CORS origins, e.g., ["http://localhost:3000"]. Default is an empty list `[]`.
- `API_KEY_NAME:` The name of the header for the API key. Default is `"X-API-KEY"`.
- `API_KEYS:` A list of allowed API keys for authentication. Default is an empty list `[]`.

These variables can be set in your environment or passed as part of your Docker configuration.

## License

This project is licensed under the terms of the [MIT](LICENSE).
