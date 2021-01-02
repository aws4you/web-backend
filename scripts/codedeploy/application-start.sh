#!/bin/bash

set -ex

. ./functions.sh

cd ${SOURCES_HOME} || exit

DJANGO_ENV=DEV GUNICORN_CMD_ARGS="--bind=127.0.0.1:8000 --workers=1" gunicorn -D core.wsgi
