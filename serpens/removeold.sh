#!/bin/sh
find /home/paycho/downloads/ -depth -mtime +120 -not -path '*/\.*' -delete
