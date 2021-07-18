#!/bin/bash

# Prepare log files and start outputting logs to stdout
#mkdir -p /usr/src/app/logs/


# echo Running tests
# exec python3 manage.py test

#echo Starting manage.py
#exec python3 manage.py runserver 0.0.0.0:8000

mkdir -p /usr/src/app/static_files/

echo "Starting Gunicorn"
exec gunicorn Spoonshot_BIM_Service.wsgi:application \
    --name bim \
    --bind 0.0.0.0:8000 \
    --workers 3 \
"$@"
