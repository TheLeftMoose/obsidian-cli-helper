#!/bin/bash

# Define source and destination directories
SOURCE_DIR="/mnt/c/Users/desck/OneDrive - Ørsted/Obsidian Vault/3-Resources (Books, articles, Townhalls, garthered infomation)/Conferences and Fairs/Reinvent24/"
DEST_DIR="/mnt/c/Users/desck/src/obsidian-cli-helper/testdata/"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  echo "Source directory $SOURCE_DIR does not exist."
  exit 1
fi

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Copy the files
cp -r "$SOURCE_DIR" "$DEST_DIR"

# Check if the copy operation was successful
if [ $? -eq 0 ]; then
  echo "Files copied successfully from $SOURCE_DIR to $DEST_DIR."
else
  echo "Failed to copy files from $SOURCE_DIR to $DEST_DIR."
  exit 1
fi