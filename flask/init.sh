#!/bin/bash

if [ $1 == 'flask' ];then
    mkdir -p /docker_data/flask/log
    rsync -av ./app/ /docker_data/flask/
    chmod 777 -R /docker_data/flask/
elif [ $1 == 'erase' ]; then
    rm -rfv /docker_data/flask
fi
