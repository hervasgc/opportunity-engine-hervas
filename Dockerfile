# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for some Python packages (like matplotlib/statsmodels)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create directories for inputs and outputs (though in Cloud Run these are ephemeral)
RUN mkdir -p inputs outputs

# Expose port 8080 (standard for Cloud Run)
EXPOSE 8080

# Healthcheck for Streamlit
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

# Command to run the app, forcing it to listen on the port provided by Cloud Run
ENTRYPOINT ["streamlit", "run", "scripts/streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
