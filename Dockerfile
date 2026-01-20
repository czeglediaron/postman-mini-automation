# Start from a minimal Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your project folder into the container's /app directory
COPY . .

# Install the Python dependency we need
RUN pip install requests

# Command to run the script automatically when the container starts
CMD ["python", "send_data.py"]
