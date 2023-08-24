#!/bin/bash
# Deleting all images
docker rmi -f $(docker images -aq)

# Deleting all containers
docker rm -f $(docker rm -aq)