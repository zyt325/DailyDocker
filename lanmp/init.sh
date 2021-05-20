#!/bin/bash
mkdir -p /docker_data/base-fx/mariadb/{data,etc}
mkdir -p /docker_data/base-fx/php/{conf,www}
cp -f mysql.cnf /docker_data/base-fx/mariadb/etc/server.cnf
mkdir -p /docker_data/base-fx/nginx/{log,www,conf}
rsync -av conf /docker_data/base-fx/nginx/