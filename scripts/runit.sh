#!/bin/sh

GUNICORN=gunicorn
PID=/var/run/web-backend-${DJANGO_ENV}.pid

APP=core:application

if [ -f $PID ]; then rm $PID; fi

cd $APP_HOME

exec $GUNICORN -c $APP_HOME/gunicorn.conf.py --pid=$PID $APP
