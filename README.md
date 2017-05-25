# FlaskReactPostgresStack

This is a boilerplate project built around these core technologies:

* Flask
* React.js
* PostgresSQL
* webpack
* Bower
* Babel
* PyJWT
* SQLAlchemy
* psycopg2
* yarn
* Flask-CORS

The responsibilities split into groups are as follows:

**Flask**

This is the web server that gives us the ability to:

1. Write REST APIs - included in the boilerplate code
2. Write web pages - static or dynamic with optional templating (Jinja2, etc.)
3. Communicate to a database - in this case, PostgresSQL via SQLAlchemy ORM & psycopg2
4. Protect our site with JWT via PyJWT - implemented in the boilerplate already
5. Optionally allow CORS to specified resources.

**React.js**

This is what we will write the frontend code in. The View in MVC.

**PostgresSQL**

This is the chosen database for this stack. While SQLite or MariaDB is also possible, PostgresSQL was chosen because it can scale to a fairly large size without intervention and is easily managed. Combined with Flask and SQLAlchemy, we can also create, migrate, and backup databases very easily.

**yarn, webpack, Bower, Babel**

These will handle management of frontend Javascript packages and compiling them to be usable by Flask. This includes installing and updating.

## Functionality Provided Out of the Box

1. REST API
2. WWW pages with React.js capability
3. JWT auth
4. PostgresSQL Database w/ automatic migrations
5. Unit Testing
6. Javascript Package Management
7. Python pip management via requirements.txt
8. webpack + yarn scripts to watch for dev changes
9. Helper scripts for commmon tasks
10. CORS support

### Babel Presets and Plugins

We use Babel to transform our Javascript code via webpack. Babel has a lot of useful options and can help us control what future features we want to support in our Javascript code. The current configuration in our webpack config has Babel supporting the following:

* As many ES5, ES6, and ES7 features as possibly supported via the [babel-preset-env](https://babeljs.io/docs/plugins/preset-env/) preset. This includes [babel-preset-es2015](https://babeljs.io/docs/plugins/preset-es2015/), [babel-preset-es2016](https://babeljs.io/docs/plugins/preset-es2016/), and [babel-preset-es2017](https://babeljs.io/docs/plugins/preset-es2017/) at the moment. FYI, this is the recommended preset to use instead of the older babel-preset-latest.
    * I've included several plugins and set the _modules_ configuration to _false_ in order to get all of the proper syntax working correctly. In particular, the [Code Splitting - Async docs for webpack](https://webpack.js.org/guides/code-splitting-async/) were key to getting all of this to work correctly.
* All the features needed to compile React code via the [babel-preset-react](https://babeljs.io/docs/plugins/preset-react/) preset.

### webpack Features

I've also implemented some basic features of webpack that should be used in just about every project:

* Code Splitting of Libraries. Specifically for our project, we need _react_ and _react-dom_. We also have the mainifest file implemented to make best use of chunks.

## Basic Setup (first run)

### Installation

```sh
cd ~/<project root>
# Install Python Requirements in desired virtualenv:
pyenv local 3.6.1
pip install -r requirements.txt
# Install frontend libraries:
# Note: You cannot use pyenv here due to this bug:
#     https://github.com/electron-userland/electron-builder/issues/638
rm .python-version
yarn
bower install
# Put pyenv back:
pyenv local 3.6.1
# Transform and leave webpack running to watch files for changes:
yarn run watch
# Now you can continue with the rest of the steps to get to a running Flask server.
```

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

Set a SECRET_KEY:

```sh
$ export SECRET_KEY="change_me"
```

### Create DB

Create the databases in `psql`:

```sh
$ psql
# create database flask_jwt_auth;
# create database flask_jwt_auth_test;
# \q
```

Create the tables and run the migrations:

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
```

### Run the Application

```sh
$ python manage.py runserver
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)

Want to specify a different port?

```sh
$ python manage.py runserver -h 0.0.0.0 -p 8080
```

#### List of Test URLs

* [Root init, Route decorator, React via Template + webpack Babel transpile](http://localhost:5000/index)
* [Root init, Route decorator, React embedded in Template](http://localhost:5000/hello)
* [Root init, Route decorator, React via Template + webpack Babel transpile](http://localhost:5000/api) - This is for testing that the REST API indeed works correctly.
* [Blueprint, MethodView, static output w/ React](http://localhost:5000/methodview/static)
* [Blueprint, MethodView, React via Template + webpack Babel transpile](http://localhost:5000/methodview/template)
* [Blueprint, Route decorator, static output](http://localhost:5000/route)
* [Blueprint, Route decorator, React via Template + webpack Babel transpile](http://localhost:5000/route/index)

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```

## Helper Scripts

These are all shortcut scripts for setting environment variables, running the server, tests, etc. They are not needed, but they are named in a way to help you quickly just do things. To use them, you must use dot space syntax to call the scripts:

```sh
cd <project root>
. ./scripts/export-development
```

This is so that the scripts that set environment variables will affect the current shell (instead of the cloned temp shell that scripts run in). This is similar to using source in bash shell but should work for all types of shells. [See explanation here.](http://stackoverflow.com/questions/496702/can-a-shell-script-set-environment-variables-of-the-calling-shell)

## Sources

This boilerplate was built through the help of these tutorials:

* [Token-Based Authentication with Flask](https://realpython.com/blog/python/token-based-authentication-with-flask/)
* [The Ultimate Flask Front-End](https://realpython.com/blog/python/the-ultimate-flask-front-end/)
* [The Ultimate Flask Front-End - Part 2](https://realpython.com/blog/python/the-ultimate-flask-front-end-part-2/)
