#!/bin/bash

# Check if the image exists
IMAGE_NAME="chat-app:$1"
if docker image inspect $IMAGE_NAME > /dev/null 2>&1; then
    # Prompt the user if they want to rebuild the image
    echo "The image '$IMAGE_NAME' already exists. Do you want to rebuild it? (y/n)"
    read REBUILD

    # If the user chooses to rebuild the image, delete the existing one
    if [[ "$REBUILD" == "y" ]]; then
        echo "Deleting the existing image..."
        docker image rm $IMAGE_NAME
    fi
fi

# Build the image
docker build -t $IMAGE_NAME .

# Push the image to Docker Hub
docker push $IMAGE_NAME