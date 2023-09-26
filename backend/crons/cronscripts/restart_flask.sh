#!/bin/sh

pkill gunicorn
echo "restart gunicorn/flask"
gunicorn -c gunicorn_conf.py app:app