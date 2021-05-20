#!/bin/bash
mkdir -p /docker_data/zabbix/{modules,alertscripts,externalscripts}
mkdir -p /docker_data/zabbix/mariadb/{data,etc}
cp -f conf/server.cnf /docker_data/zabbix/mariadb/etc