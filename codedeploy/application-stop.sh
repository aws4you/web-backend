#!/bin/bash

set -ex

. $(dirname "${BASH_SOURCE[0]}")/functions.sh

cd ${APP_HOME} || exit

if [[ $(ps ax | grep gunicorn | grep -v grep | wc -l) -gt 0  ]]; then
  killall gunicorn || :
fi
