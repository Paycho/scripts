#!/bin/bash
sudo service nginx stop
cd /etc/letsencrypt/tools
git pull origin master
/etc/letsencrypt/tools/letsencrypt-auto certonly --renew --cert-path /etc/letsencrypt/yanaduday.com -d yanaduday.com -d www.yanaduday.com -d test.yanaduday.com --agree-tos --email admin@yanaduday.com --rsa-key-size 4096 --standalone
/etc/letsencrypt/tools/letsencrypt-auto certonly --renew --cert-path /etc/letsencrypt/shodan.giml.in -d shodan.giml.in -d codiad.giml.in --agree-tos --email matt@giml.in --rsa-key-size 4096 --standalone
/etc/letsencrypt/tools/letsencrypt-auto certonly --renew --cert-path /etc/letsencrypt/mattandyana.com -d mattandyana.com -d wwww.mattandyana.com --agree-tos --email matt@giml.in --rsa-key-size 4096 --standalone
sudo service nginx start
