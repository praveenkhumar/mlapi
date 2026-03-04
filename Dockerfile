# Use Python 3.10 slim image as base for smaller image size
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt to set up dependencies
COPY requirements.txt .

# Install Python dependencies from requirements.txt without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Start the Uvicorn server running the FastAPI app on 0.0.0.0:8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]