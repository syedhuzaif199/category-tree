#!/bin/bash

echo "Installing dependencies..."

# Ensure pip is installed
python3 -m ensurepip --default-pip

# Upgrade pip
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install graphviz Faker

echo "Installation complete."
