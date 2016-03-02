#!/bin/bash
sudo service nginx stop
cd /etc/letsencrypt/tools
git pull origin master
/etc/letsencrypt/tools/letsencrypt-auto certonly --renew --cert-path /etc/letsencrypt/carnivore.giml.in --agree-tos --email matt@giml.in --rsa-key-size 4096 --standalone
sudo service nginx start
