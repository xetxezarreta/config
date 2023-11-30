#!/bin/bash

printf "START\n"
printf "Pulling from Google Drive...\n"
rclone sync gdrive: /home/user/Documents/backups/gdrive
printf "Pushing to Dropbox...\n"
printf "END\n"