#!/bin/bash

set -ex

. $(dirname "${BASH_SOURCE[0]}")/functions.sh

cd ${APP_HOME} || exit

gunicorn -c codedeploy/conf/gunicorn-${DJANGO_ENV}.conf.py -D core.wsgi

envsubst < codedeploy/conf/nginx.conf > $NGINX_AVAILABLE_APP_CONF
ln -sf $NGINX_AVAILABLE_APP_CONF $NGINX_ENABLED_APP_CONF

service nginx reload
