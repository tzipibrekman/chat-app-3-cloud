!#/bin/bash
docker build -t chat-app .
docker run  -p 5000:5000 chat-app  