#!/bin/bash

set -ex

. $(dirname "${BASH_SOURCE[0]}")/functions.sh

cd ${APP_HOME} || exit

virtualenv venv
. ./venv/bin/activate

pip3 install -r requirements.txt
python3 manage.py migrate

envsubst < codedeploy/conf/gunicorn.service > /etc/systemd/system/backend-${DJANGO_ENV}.service

systemctl daemon-reload

systemctl start backend-${DJANGO_ENV}
systemctl enable backend-${DJANGO_ENV}
