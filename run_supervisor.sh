#!/bin/bash

# Читаем переменную окружения
ENABLE_WEBSOCKET=${ENABLE_WEBSOCKET:-False}

# Создаем временный конфигурационный файл supervisord
SUPERVISORD_CONF="/etc/supervisor/conf.d/supervisord.conf"
echo "[supervisord]" > $SUPERVISORD_CONF
echo "nodaemon=true" >> $SUPERVISORD_CONF

echo "[program:django]" >> $SUPERVISORD_CONF
echo "command=python manage.py runserver 0.0.0.0:8000" >> $SUPERVISORD_CONF
echo "autostart=true" >> $SUPERVISORD_CONF
echo "autorestart=true" >> $SUPERVISORD_CONF
echo "stderr_logfile=/var/log/django_err.log" >> $SUPERVISORD_CONF
echo "stdout_logfile=/var/log/django_out.log" >> $SUPERVISORD_CONF

if [ "$ENABLE_WEBSOCKET" = "True" ]; then
  echo "[program:websocket]" >> $SUPERVISORD_CONF
  echo "command=python manage.py runwebsocketserver" >> $SUPERVISORD_CONF
  echo "autostart=true" >> $SUPERVISORD_CONF
  echo "autorestart=true" >> $SUPERVISORD_CONF
  echo "stderr_logfile=/var/log/websocket_err.log" >> $SUPERVISORD_CONF
  echo "stdout_logfile=/var/log/websocket_out.log" >> $SUPERVISORD_CONF
fi

# Запускаем supervisord
/usr/bin/supervisord -c $SUPERVISORD_CONF
