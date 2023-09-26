#!/bin/bash


# Prompt user for version and commit hash
read -p "Enter the version: " version
read -p "Enter the commit hash: " commit_hash


# Check if the image exists.
IMAGE_EXISTS=$(docker images --format="table {{.Repository}}:{{.Tag}}" | grep "chat-app:$version")

# Ask the user if they want to rebuild the image or use the existing one.
if [[ -n "$IMAGE_EXISTS" ]]; then
    echo "The image 'chat-app:$version' already exists."
    read -p "Do you want to rebuild the image? (y/n): " REBUILD_IMAGE

    if [[ "$REBUILD_IMAGE" == "y" ]]; then
        # Delete the existing image.
        docker rmi chat-app:"$version"
    fi
fi

# Build the image with a tag
docker build -t chat-app:"$version" . || { echo "Failed to build the image"; exit 1; }

# Tag the image for your registry 
docker tag chat-app:"$version" rivkarizel/chat-app:"$version" || { echo "Failed to tag for registry"; exit 1; }

# Push the image to the registry 
docker push ayalaRov/chat-app:"$version" || { echo "Failed to push to registry"; exit 1; }

# Ask the user if they want to tag and push the image to the GitHub repository.
read -p "Do you want to tag and push the image to the GitHub repository? (y/n): " TAG_GITHUB_REPO

if [[ "$TAG_GITHUB_REPO" == "y" ]]; then
    # Check if the commit hash exists.
    COMMIT_HASH=$(git rev-parse HEAD)

    if [[ -n "$COMMIT_HASH" ]]; then
        # Tag the image with the commit hash.
        git tag "$version" "$commit_hash"

        # Push the tag to the GitHub repository.
        git push origin "$version"
    else
        echo "The commit hash does not exist."
    fi
fi

echo "Deployment successful!"
