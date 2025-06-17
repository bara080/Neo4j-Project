#!/bin/bash

# Exit if any command fails
set -e

# Step 1: Create README
echo "# Neo4j-Project" >> README.md

# Step 2: Initialize git and commit
git init
git add README.md
git commit -m "first commit"

# Step 3: Set branch and remote
git branch -M main
git remote add origin https://github.com/bara080/Neo4j-Project.git

# Step 4: Push to GitHub
git push -u origin main

echo "Neo4j project repository initialized and pushed!"
