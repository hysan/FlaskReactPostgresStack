# About FlaskReactPostgresStack

## Folder and File Structure

```
┌─[mike@Daisy] - [/Users/mike/Workspace/Python/Flask/FlaskReactPostgresStack] - [2017-05-11 04:34:47]
├ [git:(master) ✗]
└─⚡ tree
.
├── ABOUT.md
├── LICENSE
├── README.md
├── TODO.md
├── bower.json
├── manage.py
├── package.json
├── webpack.config.js
├── yarn.lock
├── .babelrc
├── .bowerrc
├── .gitignore
├── .python-version
├── .travis.yml
├── .vscode
│   └── <bunch of folders>
├── migrations
│   └── <bunch of folders>
├── node_modules
│   └── <bunch of folders>
├── project
│   ├── __init__.py
│   ├── server
│   │   ├── __init__.py
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   └── views.py
│   │   ├── config.py
│   │   ├── methodview
│   │   │   ├── __init__.py
│   │   │   └── views.py
│   │   ├── models.py
│   │   ├── route
│   │   │   ├── __init__.py
│   │   │   └── views.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── style.css
│   │   │   └── scripts
│   │   │       ├── js
│   │   │           ├── main.js
│   │   │       │   └── api.js
│   │   │       └── jsx
│   │   │           ├── main.js
│   │   │           └── api.js
│   │   └── templates
│   │       ├── hello.html
│   │       ├── index.html
│   │       └── api.html
│   └── tests
│       ├── __init__.py
│       ├── base.py
│       ├── helpers.py
│       ├── test__config.py
│       ├── test_auth.py
│       ├── test_example.py
│       └── test_user_model.py
├── requirements.txt
├── scripts
│   ├── export-development
│   ├── export-secret-key
│   ├── initialize-databases
│   ├── install-python-requirements
│   ├── migrate-databases
│   ├── run-server
│   ├── run-tests
│   └── run-tests-with-coverage
└── tmp
    └── <bunch of folders>
```

### Folders Explanation

* **.vscode**
    * **.gitignore**
    * This holds configurations for your Visual Studio Code instance/project/workspace.
* **migrations**
    * **.gitignore**
    * Generated when you create and/or migrate databases via **manage.py**.
* **node_modules**
    * **.gitignore**
    * Generated when you run `yarn`.
    * Contains all of the modules defined in **package.json** along with their dependencies.
* **project**
    * Directory containing all the source files for the Flask project.
    * Any new source code you add will primarily be here.
    *  **server**
        * Contains Flask python source files, modules, static files (css, assets, html), and Javascript files.
        * You will be creating several module folders in here as a way to separate and organize your Flask project.
        * **auth**
            * Module that handles JWT auth for REST APIs.
        * **methodview**
            * Example module showing how to use Blueprints via MethodView.
            * This is the preferred method for creating REST APIs.
            * However, you can use this to do normal web views as well.
        * **route**
            * Example module showing hot to use Blueprints along with the normal route decorators.
            * This is probably the best way to separate normal web view code cleanly.
        * **static**
            * Holds all traditional static files that need to be served by Flask.
            * **css**
                * Holds all css files.
            * **scripts**
                * Holds all Javascript and related files.
                * **js**
                    * Straight up Javascript files written by you.
                    * Also the place where `webpack` will place the transformed *jsx* files.
                * **jsx**
                    * Holds all React.js files.
                    * Files here will be transformed by running `webpack -p`.
        * **templates**
            * Holds all *HTML* files.
            * These are the files that can be rendered directly via Flask's `render_template` function.
    * **tests**
        * Holds all Python unit tests for the Flask project.
* **scripts**
    * Holds my shortcut shell scripts for running common development commands.
    * Also has scripts for setting environment variables.
* **tmp**
    * **.gitignore**
    * A temp folder that is generated when you run unit tests with code coverage.

### Files Explanation

Only key, non-self explanatory files will be covered.

* **.python-version**
    * This is actually not really needed. It's a pyenv config file for defining what version of Python/virtualenv to use for this folder.
    * It is set using `pyenv local <env>`.
    * I included it because it is a good self-documenting way of telling me what version of Python this boilerplate project is configured and tested against.
* **requirements.txt**
    * Contains a list of all Python modules needed for this project.
    * Installed when you run `pip install -r requirements.txt`.
* **manage.py**
    * Flask manager script for running various tasks and ultimately running the server.
* **package.json**
    * Manages all the backend Javascript dependencies that this project has.
    * For example: bower, webpack, babel, etc.
    * These are all node packages that will be installed when you run `yarn`.
* **yarn.lock**
    * Has information about dependencies that you need for yarn.
    * Need to check this into version control.
* **bower.json**
    * Configuration for Bower.
    * Bower is what is used to install and manage frontend dependencies.
    * For example: react, bootstrap, etc.
* **.babelrc**
    * Configuration for Babel.
    * [Check the docs](https://babeljs.io/docs/usage/babelrc/) to see how to configure it.
    * Specifically, I'm using the [babel-preset-env](http://babeljs.io/docs/plugins/preset-env/) which has many options.
    * You need to configure this file in conjunction with your **webpack.config.js** to get Babel to work correctly. And yes, there is a lot that looks like duplicate configuration but it's needed.
* **.bowerrc**
    * Config file for Bower to define where to place your **bower_components** folder.
* **webpack.config.js**
    * All configuration for webpack - plugins, transforms, etc.
    * Shortcuts for the various webpack commands will be added to **package.json** as `yarn run` scripts.
    * For this project, webpack is used with Babel + plugins to transform the files in **project/server/static/scrips/jsx** into Javascript files. It also separates out vendor files like _react_ and _react-dom_ so code can be shared.
* **project/server/config.py**
    * Contains all configuration for the Flask app.
    * Of importance are the PostgreSQL configs and your SECRET_KEY.
* **project/server/models.py**
    * Contains all of your database models.
    * This is shared across all of your view modules.
    * *TODO*: If the models grow to be too large and complex, it is worth considering making this into it's own module folder with separate model files.
* **project/tests/test_something.py**
    * Every test file will be run as a unit test with `python manage.py test` or `python manage.py cov`.
    * My naming convention will be to use *test_* as the prefix to my unit test files.

