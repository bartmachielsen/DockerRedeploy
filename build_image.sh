#!/bin/bash
echo "Building image for repository $3"
docker build --tag=$2 $1

# if [ "$(docker ps -q -f name=$3)" ]; then
#     docker create --volumes-from $3 --name $3_copy $2
#     echo "Removing old container"

#     if [ "$(docker ps -aq -f status=running -f name=$3)" ]; then
#         docker stop $3
#         docker rm $3
#         docker rename $3_copy $3
#         docker start $3
#     else
#         docker rm $3
#         docker rename $3_copy $3
#     fi
# else
#     docker create --name $3 $2
# fi