export DJANGO_ENV=${DEPLOYMENT_GROUP_NAME:-LOCAL}
export APP_HOME=$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. >/dev/null 2>&1 && pwd)

case "$DJANGO_ENV" in
PROD)
  export APP_PORT=8000
  export APP_DOMAIN=api.cloud-init.ml
  ;;
DEV)
  export APP_PORT=8001
  export APP_DOMAIN=api.dev.cloud-init.ml
  ;;
*)
  echo ERROR: You should handle your deployment group here
  exit 1
  ;;
esac

export NGINX_CONF=backend-${DJANGO_ENV}.conf
export NGINX_AVAILABLE_APP_CONF=/etc/nginx/sites-available/${NGINX_CONF}
export NGINX_ENABLED_APP_CONF=/etc/nginx/sites-enabled/${NGINX_CONF}
