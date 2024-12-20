# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install build tools
RUN apt-get update && apt-get install -y \
    gcc \
    make \
    build-essential \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python service code to the working directory
COPY app /app

# Expose port 5000 to allow external access
EXPOSE 5000

# Command to run the Python service
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]