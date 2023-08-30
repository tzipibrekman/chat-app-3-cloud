#!/bin/bash

# Check if the user has provided a version and commit hash
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: deploy.sh <version> <commit hash>"
  exit 1
fi

# Build the Docker image
docker build -t my-chatapp:$1 .

# Tag the Docker image with the commit hash
docker tag my-chatapp:$1 my-chatapp:$2


# Push the Docker image to GitHub Container Registry
echo "Pushing Docker image to GitHub Container Registry..."
git tag $1 $2
git push origin $1
docker push my-chatapp:$1
docker push my-chatapp:$2


echo "Done!"