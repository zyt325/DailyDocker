#!/bin/bash

if [ $1 == 'binlog' ];then
    mkdir -p /docker_data/binlog/
    rsync -av ./app/ /docker_data/binlog/
    chmod 777 -R /docker_data/binlog/
elif [ $1 == 'erase' ]; then
    rm -rfv /docker_data/binlog
fi
