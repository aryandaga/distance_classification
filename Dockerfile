# Use the latest Python image
FROM python:3.11

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY . .

# Install Python dependencies, including Matplotlib
RUN pip install --no-cache-dir numpy pandas scikit-learn wandb opencv-python matplotlib

# Run the script
CMD ["python", "distance_classification.py"]
