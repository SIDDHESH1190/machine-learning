#!/bin/bash

echo "Setting up Machine Learning Project..."

# Create conda environment
conda create -n ml-project python=3.13 -y

# Activate environment
conda activate ml-project

# Install packages
conda install -c conda-forge numpy pandas scikit-learn matplotlib seaborn jupyter -y

# Install pip packages
pip install -r requirements.txt

echo "Setup completed! Activate environment with: conda activate ml-project"