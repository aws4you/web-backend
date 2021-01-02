#!/bin/bash

set -ex

. $(dirname "${BASH_SOURCE[0]}")/functions.sh

cd ${APP_HOME} || exit

if [[ $(ps ax | grep codedeploy/conf/gunicorn-${DJANGO_ENV}.conf.py | grep -v grep | wc -l) -gt 0  ]]; then
  kill $(ps ax | grep codedeploy/conf/gunicorn-${DJANGO_ENV}.conf.py | grep -v grep | awk '{print $1}')
fi
