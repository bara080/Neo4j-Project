#!/bin/bash
set -e

# Step 1: Init Git if not already
if [ ! -d .git ]; then
  git init
  echo "# Neo4j-Project" > README.md
  git add README.md
  git commit -m "initial commit"
fi

# Step 2: Create js branch and JS project
git checkout -B js
mkdir -p neo4j-js
cd neo4j-js
npm init -y
npm install neo4j-driver
touch index.js
cd ..
git add neo4j-js
git commit -m "add JS project"

# Step 3: Create python branch and Python project
git checkout -B python
rm -rf neo4j-js
mkdir -p neo4j-python
cd neo4j-python
conda create -y -n neo4j-python-env python=3.10
conda activate neo4j-python-env || source activate neo4j-python-env
pip install neo4j
touch main.py
conda deactivate
cd ..
git add -A
git commit -m "add Python project and remove JS project"

echo "✅ js and python branches created with isolated projects."
