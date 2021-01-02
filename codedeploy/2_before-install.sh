#!/bin/bash

set -ex

. $(dirname "${BASH_SOURCE[0]}")/functions.sh

cd ${APP_HOME} || exit

virtualenv venv
. ./venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate
