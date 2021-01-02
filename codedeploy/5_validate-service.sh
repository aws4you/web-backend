#!/bin/bash

set -ex

. $(dirname "${BASH_SOURCE[0]}")/functions.sh

cd ${APP_HOME} || exit

curl -f --unix-socket $GUNICORN_SOCKET_PATH http://127.0.0.1/admin/