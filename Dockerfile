# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt and the application code to the container
COPY requirements.txt ./
COPY app.py ./
COPY templates/ ./templates/
COPY static/ ./static/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application using Flask's built-in server
CMD ["python", "app.py"]
