# bffbook
Autenticação com Custom User usando o Django.

## Installation
> **_NOTE:_**  You must have PostgreSQL installed. If you don't, run the commands below:

Install dependencies to work with Django and PostgreSQL: 
```shell
    sudo apt-get install libpq-dev python-dev
    sudo apt-get install postgresql postgresql-contrib
```
1. Clone the [repo](https://github.com/iasmini/bffbook):
```shell
    git clone https://github.com/iasmini/bffbook
```
2. Access the root directory (bffbook) and run the command:
> **_NOTE:_**  It's recommended doing it within a virtual environment.
```shell
    pip install -r requirements.txt
```
3. Create the database:
```shell
    ./scripts/create_db.sh
```

## How to use it
1. Access the root directory (bffbook) and run the command:
```shell
    python manage.py migrate --noinput
    python manage.py runserver
```
or, if you have Make installed:
```shell
    make migrate
    make run
```
2. It will be available on: http://127.0.0.1:8000/
