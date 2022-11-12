#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py makemigrations core
python manage.py migrate core
python manage.py makemigrations register
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi