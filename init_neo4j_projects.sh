#!/bin/bash

# Exit on error
set -e

# ---- Python Setup using Conda ----
echo "Setting up neo4j-python (using conda)..."
mkdir -p neo4j-python
cd neo4j-python

# Create and activate conda environment
conda create -y -n neo4j-python-env python=3.10
conda activate neo4j-python-env || source activate neo4j-python-env

# Install Neo4j driver
pip install neo4j

# Create main Python script
touch main.py

# Deactivate conda env
conda deactivate
cd ..

# ---- JavaScript Setup ----
echo "Setting up neo4j-js..."
mkdir -p neo4j-js
cd neo4j-js
npm init -y
npm install neo4j-driver
touch index.js
cd ..

echo "Neo4j Python (conda) and JS projects initialized successfully!"
