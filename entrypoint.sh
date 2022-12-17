#!/bin/sh

echo 'Running collectatic...'
python manage.py collectstatic --no-input --settings=agency.settings.production

echo 'Applying migrations'
python manage.py migrate --settings=agency.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS-MODULE=agency.settings.production agency.wsgi:application --bind 0.0.0.0:8000