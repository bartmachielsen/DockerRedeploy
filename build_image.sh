#!/bin/bash
echo "Building image for repository $3"
docker build --tag=$2 $1

if [ "$(docker ps -q -f name=$3)" ]; then
    # if [ "$(docker ps -aq -f status=exited -f name=$3)" ]; then
        
    # else
    #     docker create --name $3 $2
    # fi
    
    docker create --volumes-from $3 --name $3_copy $2
    echo "Removing old container"
    docker rm $3
    docker rename $3_copy $3
else
    docker create --name $3 $2
fi