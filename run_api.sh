#/bin/sh
python djangochallenge/manage.py makemigrations

python djangochallenge/manage.py migrate

cd djangochallenge

python manage.py test

gunicorn djangochallenge.wsgi:application --bind 0.0.0.0:8000