# RateMyClass Django

Django version of RateMyClass

## Installation

### Setup the virtualenv

```
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Setup the database

```
./manage.py migrate
./manage.py createsuperuser
```

### Load fixtures

```
python manage.py loaddata fixtures.json
```

## Usage

```
./manage.py runserver
```
