#!/bin/bash
mkdir -p /docker_data/mariadb/{data,etc}
cp -f conf/server.cnf /docker_data/mariadb/etc