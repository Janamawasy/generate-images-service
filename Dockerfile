# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire current directory into the container at /app
COPY . .

# Expose port 8003 to the outside world
EXPOSE 8003

# Command to run the FastAPI application with uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8003"]

