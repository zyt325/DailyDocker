#!/bin/bash

if [[ "$1" =~ 'init' ]];then
mkdir -p /sentry/{pgdata,etc,sentry_data}
chmod 777 /sentry/{pgdata,etc,sentry_data}
SECRET_KEY=$(docker-compose run --rm sentry-web config generate-secret-key 2> /dev/null | tail -n1 | sed -e 's/[\/&]/\\&/g')
sed -i "/^system.secret-key/d" /sentry/etc/config.yml
echo "system.secret-key: '$SECRET_KEY'" >> /sentry/etc/config.yml
sed -i -e 's/^SENTRY_SECRET_KEY=.*$/SENTRY_SECRET_KEY='"$SECRET_KEY"'/' .env
elif [[ "$1" =~ 'set' ]];then
docker-compose run --rm  sentry-web upgrade
elif [[ "$1" =~ 'up' ]];then
docker-compose up -d
elif [[ "$1" =~ 'stop' ]];then
docker-compose stop -d
elif [[ "$1" =~ 'remove' ]];then
docker-compose down
fi
