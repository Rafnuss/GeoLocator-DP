#!/bin/bash

# run this script with ./assets/create_symbolic_link.sh 

# Move into the _data directory
cd _data || { echo "Directory _data not found. Exiting."; exit 1; }

# Find and link all *table-schema.json and *profile.json files from the project root
for file in ../*table-schema.json ../*profile.json; do
  # Check if the file exists (in case no files match the pattern)
  if [ -e "$file" ]; then
    # Get the filename without the path
    filename=$(basename "$file")
    
    # Create a symbolic link in the _data directory
    ln -s "$file" "$filename"
    echo "Created symlink for $filename"
  fi
done