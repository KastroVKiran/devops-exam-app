# Dockerfile

# Use Python's official image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 5000 for Flask to run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
