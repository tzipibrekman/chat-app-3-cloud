#!bin/bash
# Stop and remove the container
docker stop chat-app
docker rm chat-app

# Remove the Docker image
docker rmi chat-app
