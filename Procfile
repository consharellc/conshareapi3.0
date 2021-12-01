web: gunicorn conshareapi.wsgi --log-file -
release: python manage.py migrate
release: python manage.py migrate --database=message