# # Use official Python image
# FROM python:3.10-slim

# # Set working directory inside container
# WORKDIR /app

# # Copy requirements.txt first (for caching layers)
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application
# COPY . .

# # Expose Flask port
# EXPOSE 5000

# # Run Flask app
# CMD ["python", "app.py"]


# FROM python:3.11-slim

# WORKDIR /app
# COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .

# CMD ["python", "app.py"]

# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (Railway will override with PORT env)
EXPOSE 5000

# Start the app with Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

