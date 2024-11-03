#!/bin/bash

NAMENODE_CONTAINER="hdfs_project-namenode-1"

# Create directories and set permissions 
# docker exec -it $NAMENODE_CONTAINER hadoop fs -mkdir -p /user/hadoop && \
docker exec -it $NAMENODE_CONTAINER hadoop fs -mkdir -p /test && \
docker exec -it $NAMENODE_CONTAINER hadoop fs -chmod -R 777 /test