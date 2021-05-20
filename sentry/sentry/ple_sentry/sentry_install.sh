#!/bin/bash
if [[ "$1" =~ 'build' ]];then
docker build -t harbor.base-fx.com/itd/sentry-ldap:8.22.0 .
elif [[ "$1" =~ 'init' ]];then
rm -rfv /docker_data/sentry
mkdir -p /docker_data/sentry/{pgdata,etc,sentry_data,sentry-smtp,sentry-smtp-log}
chown 999.999 /docker_data/sentry/pgdata
chmod 777 /docker_data/sentry/{pgdata,etc,sentry_data}
cp -f config.yml /docker_data/sentry/etc/
cp -f sentry.conf.py /docker_data/sentry/etc/
cp .env.sample .env
SECRET_KEY=$(docker-compose run --rm sentry-web config generate-secret-key 2> /dev/null | tail -n1 | sed -e 's/[\/&]/\\&/g')
sed -i "/^system.secret-key/d" /docker_data/sentry/etc/config.yml
echo "system.secret-key: '$SECRET_KEY'" >> /docker_data/sentry/etc/config.yml
sed -i -e 's/^SENTRY_SECRET_KEY=.*$/SENTRY_SECRET_KEY='"$SECRET_KEY"'/' .env

#docker-compose -f sentry.yml run --rm  sentry-web init
elif [[ "$1" =~ 'set' ]];then
docker-compose run --rm  sentry-web upgrade
elif [[ "$1" =~ 'up' ]];then
docker-compose up -d
elif [[ "$1" =~ 'stop' ]];then
docker-compose stop -d
elif [[ "$1" =~ 'remove' ]];then
docker-compose down
fi
