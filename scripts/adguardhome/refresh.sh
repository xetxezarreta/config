#!/bin/bash

docker pull adguard/adguardhome
docker stop adguardhome
docker rm adguardhome

docker run --name adguardhome\
    --restart unless-stopped\
    -v /home/ubuntu/adguardhome/workdir:/opt/adguardhome/work\
    -v /home/ubuntu/adguardhome/confdir:/opt/adguardhome/conf\
    -p 53:53/tcp -p 53:53/udp\
    -p 80:80/tcp -p 3000:3000/tcp\
    -d adguard/adguardhome