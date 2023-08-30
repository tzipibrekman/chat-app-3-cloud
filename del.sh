# Stop and remove the container
read -p "enter container name: " cn
read -p "enter img name: " img
docker stop "$cn"
docker rm "$cn"

# Remove the Docker image
docker rmi "$img"
