FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend application files
COPY backend/ .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
