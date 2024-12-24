# Use a Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./src /app

# Expose port for Flask
EXPOSE 5000

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

