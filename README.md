# Talpor test project

This is a test project for talpor.

Requirements: (in requirements.txt file)

- Django
- djangorestframework
- gunicorn

For development we use these packages:

- black
- isort

## Usage:

For running in a development environment you could use this way:

```
python manage.py migrate
python manage.py loaddata
python manage.py runserver
```

And then open in browser:

- http://localhost:8000/api/orders
- http://localhost:8000/api/orders/1

You could filter orders by `status`, `date` and `total` as follows:


- http://localhost:8000/api/orders/?status=pending
- http://localhost:8000/api/orders/?date=2020-12-28
- http://localhost:8000/api/orders/?total=100

## Docker

It also has a Dockerfile and docker-compose.yml files to use, so you only need to run:

```
cd /path/to/talpor
docker-compose up
```

And go to the browser.


