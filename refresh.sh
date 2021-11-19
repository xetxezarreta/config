#!/bin/bash
printf "START\n"
printf "Pulling from Google Drive...\n"
rclone sync gdrive: /home/xetxezarreta/Documentos/backups/gdrive
printf "Pushing to Dropbox...\n"
printf "END\n"
