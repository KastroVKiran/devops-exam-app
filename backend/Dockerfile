FROM python:3.10-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend application files (everything inside backend)
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
