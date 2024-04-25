#!/bin/sh

curl -s https://bit.ly/1O72s3U | grep -o '<a href=".*">' | cut -d'"' -f2