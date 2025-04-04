# Dockerfile

# Use Python's official image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask to run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
