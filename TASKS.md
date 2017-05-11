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
>     create database flask_jwt_auth
>     create database flask_jwt_auth_test
>     \q

python manage.py create_db
python manage.py db init
python manage.py db migrate
```

### Update/Migrate Tables in Existing Database

```sh
python manage.py db migrate
```

### Set Environment Variables

```sh
export APP_SETTINGS="project.server.config.DevelopmentConfig"
# OR
export APP_SETTINGS="project.server.config.ProductionConfig"

export SECRET_KEY="change_me"
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

One of our required node modules [doesn't play nicely with pyenv & shims](https://github.com/electron-userland/electron-builder/issues/638), so we need to disable pyenv while installing and then put it back:

```sh
cd <project root>
rm .python-version
npm install
pyenv local 3.6.1
```

### Install or Update Frontend Components with Bower

Installation can be done in one of two ways:

1. Run `bower install <package_name> --save` for each package (the `--save` flag adds the dependencies (name and version) to the **bower.json** file.).
2. Update the **bower.json** file directly with each dependency (again, name and version) and then run `bower install` to install all dependencies from the file.

Updating can be done by editing the versions in **bower.json**. Then rerunning `bower install` (optionally delete the **bower_components** folder).

