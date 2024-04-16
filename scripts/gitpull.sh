#!/bin/bash

# Define the directory where your repositories are located
#MAIN_DIRECTORY="/path/to/main_directory"
MAIN_DIRECTORY="."

# Change to the main directory
cd "$MAIN_DIRECTORY" || { echo "Directory $MAIN_DIRECTORY not found"; exit 1; }

# Iterate over each directory in the main directory
for repo in */; do
    # Check if it's a git repository
    if [ -d "$repo/.git" ]; then
        echo "Pulling changes in $repo"
        # Change directory to the repository and perform git pull
        (cd "$repo" && git pull)
    else
        echo "$repo is not a git repository"
    fi
done
