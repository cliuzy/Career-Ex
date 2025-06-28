
# # Use the official python:3.9 base image as the runtime environment
# FROM python:3.9-slim

# # Set working directory to /app
# WORKDIR /app

# # Install dependencies using pip
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy source code into the container
# COPY . .

# # Expose port 8000 for production use, assuming it's typically used as the default
# EXPOSE 8000

# # Set environment variable 'DJANGO_SETTINGS_MODULE' to point to settings.py of our app
# ENV DJANGO_SETTINGS_MODULE=appsettings

# # Run the application when the container starts
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]