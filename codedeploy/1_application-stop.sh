#!/bin/bash

set -ex

. $(dirname "${BASH_SOURCE[0]}")/functions.sh

cd ${APP_HOME} || exit

systemctl stop backend-${DJANGO_ENV} ||:

