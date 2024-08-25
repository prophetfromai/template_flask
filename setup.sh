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

# Upgrade pip and install Python dependencies
echo "Upgrading pip and installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
