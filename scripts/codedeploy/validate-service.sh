#!/bin/bash

set -ex

. ./functions.sh

cd ${SOURCES_HOME} || exit

wget -q http://127.0.0.1:8000
