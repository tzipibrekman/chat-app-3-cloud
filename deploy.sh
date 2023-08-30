#!/bin/bash

git tag $1 $2
git push origin $1

docker build -t chat-app:$1 .
docker push chat-app:$1