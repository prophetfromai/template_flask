#!/bin/bash

# Update package list and install curl
apt-get update && apt-get install -y curl

# Download and install the Google Cloud SDK
echo "Downloading and installing Google Cloud SDK..."
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz
tar -xf google-cloud-cli-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh -q

# Add gcloud to PATH
echo "source /workspace/google-cloud-sdk/path.bash.inc" >> /home/vscode/.bashrc
source /workspace/google-cloud-sdk/path.bash.inc

# Initialize gcloud (non-interactive setup; adjust as needed)
echo "Initializing Google Cloud SDK..."
gcloud init --skip-diagnostics

# Create a virtual environment
echo "Creating a Python virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Upgrade pip in the virtual environment
echo "Upgrading pip in the virtual environment..."
pip install --upgrade pip

# Install Python dependencies from requirements.txt in the virtual environment
echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

# Inform the user the setup is complete
echo "Setup complete. Virtual environment 'venv' is activated and dependencies are installed."
