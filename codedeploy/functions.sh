export DJANGO_ENV=${DEPLOYMENT_GROUP_NAME:-LOCAL}
export APP_HOME=$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. >/dev/null 2>&1 && pwd)

