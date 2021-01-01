#!/bin/bash

set -ex

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")"/../.. >/dev/null 2>&1 && pwd)" || exit

# Install requirements
pip3 install -r requirements.txt

echo "before install"