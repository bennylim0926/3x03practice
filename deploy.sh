#!/usr/bin/env sh

set -x
docker build -t flask-app .
docker run -d -p 8001:8001 --name flask-app flask-app
sleep 1
set +x

echo 'visit http:localhost:8001 to your flask app'