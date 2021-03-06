# Common Development Tasks

## Development

### Run Flask Web Server

```sh
python manage.py runserver
# OR
python manage.py runserver -h 0.0.0.0 -p 8080
```

### Run Python Unit Tests

```sh
python manage.py test
# OR
python manage.py cov
```

### Create Database and Tables

```sh
psql
>     create database flask_jwt_auth;
>     create database flask_jwt_auth_test;
>     \q

python manage.py create_db
python manage.py db init
python manage.py db migrate
```

### Update/Migrate Tables in Existing Database

```sh
python manage.py db migrate
python manage.py db upgrade
```

### Set Environment Variables

```sh
export APP_SETTINGS="project.server.config.DevelopmentConfig"
# OR
export APP_SETTINGS="project.server.config.ProductionConfig"

export SECRET_KEY="change_me"
```

### Complete Clean and Reset

```sh
cd <project root>
rm -rf node_modules
rm -rf migrations
rm -rf tmp
# Drop database tables using pgAdmin 4.
```

## Python

### Set virtualenv

I use *pyenv* for managing things so to set your virtualenv (for example to 3.6.1), do this:

```sh
cd <project root>
pyenv local 3.6.1
```

### Install

```sh
pip install -r requirements.txt
```

### Update requirements.txt

After running something like `pip install <something>` to add something to the virtualenv, you can update your **requirements.txt** file with:

```sh
pip freeze > requirements.txt
```

## Javascript

### Install node modules

```sh
cd <project root>
yarn
```
