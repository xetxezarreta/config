# xubuntu_minimal

## Install packages
Packages to install in a Xubuntu minimal install.

```console
sudo apt install \
  engrampa \
  thunar-archive-plugin \
  git \
  atril \
  xfce4-taskmanager \
  texlive-full \
  mousepad
```
## Rclone Google Drive backup to local
```console
#!/bin/bash
printf "START\n"
printf "Pulling from Google Drive...\n"
rclone sync gdrive: /home/xetxezarreta/Documentos/backups/gdrive
printf "Pushing to Dropbox...\n"
printf "END\n"
```
