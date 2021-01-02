#!/bin/bash

set -ex

. ./functions.sh

cd ${SOURCES_HOME} || exit

pip3 install -r requirements.txt

python3 manage.py migrate
