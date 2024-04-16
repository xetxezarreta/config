#!/bin/bash

# Function to display messages with timestamps
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1"
}

log "START"
log "Pulling from Google Drive..."

# Check if rclone is installed
if ! command -v rclone &> /dev/null; then
    log "Error: rclone is not installed. Please install rclone and configure it."
    exit 1
fi

# Sync with Google Drive
rclone sync gdrive: ./gdrive

# Check if sync was successful
if [ $? -eq 0 ]; then
    log "Sync completed successfully."
else
    log "Error: Sync failed."
    exit 1
fi

log "END"
