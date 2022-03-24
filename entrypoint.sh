#! /bin/bash

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

# daphne -b 0.0.0.0 -p 8001 equdb.asgi:application
hypercorn --reload --bind 0.0.0.0:8001 core.asgi:application
# daphne -b 0.0.0.0 -p 8001 yoga.asgi:application -v2