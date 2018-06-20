#! /bin/sh

python manage.py makemigrations model
python manage.py migrate
#python manage.py create_superuser
