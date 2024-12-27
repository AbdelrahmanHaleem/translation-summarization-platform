# Use a Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py /app/

# Set the Flask app environment variable
ENV FLASK_APP=app.py

# Expose the application port
EXPOSE 8001

#Add a health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 CMD curl -f http://localhost:8001/health || exit 1


# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8001"]