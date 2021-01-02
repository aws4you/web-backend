#!/bin/bash

set -ex

. $(dirname "${BASH_SOURCE[0]}")/functions.sh

cd ${APP_HOME} || exit

gunicorn -c codedeploy/conf/gunicorn-${DJANGO_ENV}.conf.py -D core.wsgi
