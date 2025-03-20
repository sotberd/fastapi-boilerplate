# Python version
ARG PYTHON_VERSION=3.11-slim

# Use the official Python image as the base image
FROM python:${PYTHON_VERSION}

# Update and upgrade the packages in the base image
RUN apt-get update && apt-get upgrade -y

# Set environment variables to prevent Python from writing pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install the dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 8000 for the FastAPI application
EXPOSE 8000
