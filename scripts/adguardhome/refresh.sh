#!/bin/bash

WORKDIR=/home/ubuntu/adguardhome/workdir
CONFDIR=/home/ubuntu/adguardhome/confdir

docker ps -q --filter name=adguardhome > /dev/null 2>&1 && {
  # Container is running, stop and remove it
  docker stop adguardhome
  docker rm adguardhome
}

# Pull the image (check for errors)
docker pull adguard/adguardhome || exit 1

docker run --name adguardhome \
  --restart unless-stopped \
  -v $WORKDIR:/opt/adguardhome/work \
  -v $CONFDIR:/opt/adguardhome/conf \
  -p 53:53/tcp -p 53:53/udp \
  -p 80:80/tcp -p 3000:3000/tcp \
  -d adguard/adguardhome

# Check for errors in docker run
if [ $? -ne 0 ]; then
  echo "Error starting Adguard container"
  exit 1
fi

echo "Adguard Home container started successfully"
