# TODO

Possible improvements to be made to the boilerplate project.

* Integrate [gulp-livereload](https://github.com/vohof/gulp-livereload).
* Integrate some sort of css framework like Bootstrap.
* Include boilerplate code for session based logins for normal web views.
* Example code in React for keeping [long term sessions](https://www.reddit.com/r/reactjs/comments/4dw782/what_is_the_best_way_to_maintain_users_session_in/) (cookies, local storage, etc.).
* Refactor JWT code to use decorators (more DRY).
    * OR refactor to use [@app.before_request to handle JWT](http://www.fudzilla.tech/2016/12/12/flask-rest-service-with-jwt/).
* Include examples of how to restrict REST API endpoints with JWT decorators both within the auth module and outside of it.
* Boilerplate for Web Sockets that are projected by some sort of security (JWT or otherwise).
* Unit tests that hit the REST API externally. Something that can be used with CI.
* External API access example code.
* DEPLOYMENT.md doc with setup, backup, and restore instructions.
* Social/Oauth example code.
* Extend JWT registration to handle email confirmation as well.
* Add caching.
* Add example csv / Google Sheets parser and uploader to pre-populate databases.
* Integrate [Flask-Login](https://flask-login.readthedocs.io/en/latest/).
* Integrate [Flask-Security](https://pythonhosted.org/Flask-Security/) if I find that it's useful.
* Integrate [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/).
* Integrate [Flask-API](http://www.flaskapi.org) though this is probably too much. This really is an optional thing.
* Integrate [Flask-RESTful](https://flask-restful.readthedocs.io/en/0.3.5/) though this is probably a bit much as straight Flask with Blueprints already works very well.
* Replace [gulp with webpack](https://www.fullstackreact.com/articles/react-tutorial-cloning-yelp/#building-_real_-routes) - [HN Discussion on React Tutorial: Cloning Yelp Tutorial](https://news.ycombinator.com/item?id=11778663)
* Integrate [socket.io](https://github.com/raineroviir/react-redux-socketio-chat).
* [Fetch / POST / GET example code](https://github.com/pusher-community/react-realtime-chat) or a util library for common functions.
* [AJAX example code in React](https://www.reddit.com/r/reactjs/comments/4pbq2x/why_isnt_ajax_present_in_many_examples_of/).
* [Implement CORS](https://keathmilligan.net/jwt-authentication-with-flask-and-angular-2-a-simple-end-to-end-example/) since that probably will be needed for React Native communication.
* Add example middleware for logging.

Things to read to better understand Flask, React, etc. These may lead to restructuring the project for better clarity and flexibility in the future.

* [flask-restless-security](https://github.com/graup/flask-restless-security) - This project is basically the same exact thing that I want to accomplish with my boilerplate project. This should be the first thing to compare against.
* [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [Flask-Potion: REST framework for Flask, now supports Peewee](https://news.ycombinator.com/item?id=10284056)
* [Looking For Flask Restful API Design Examples](https://www.reddit.com/r/flask/comments/2ggv04/looking_for_flask_restful_api_design_examples/)
* [http://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files](http://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files)
* [URL prefixing when registering Flask Blueprints](http://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files)
* [Centralizing and importing routes into a single file](https://gist.github.com/Jaza/61f879f577bc9d06029e)
* [Using before_request in the app or in a Blueprint](https://news.ycombinator.com/item?id=11124742)
* [Python Flask and React](https://www.reddit.com/r/reactjs/comments/5fr08m/python_flask_and_react/)
* [About Flask Blueprints](http://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly)
* [Official Flask docs on Method Views for APIs](http://flask.pocoo.org/docs/0.12/views/#method-views-for-apis)
* [Python Generators for Lazy Iteration of Data](https://realpython.com/blog/python/introduction-to-python-generators/)
* [Testing External APIs With Mock Servers](https://realpython.com/blog/python/testing-third-party-apis-with-mock-servers/)
* [Mocking External APIs in Python](https://realpython.com/blog/python/testing-third-party-apis-with-mocks/)
* [Getting Started With the Slack API Using Python and Flask](https://realpython.com/blog/python/getting-started-with-the-slack-api-using-python-and-flask/)
* [Python Virtual Environments - a Primer](https://realpython.com/blog/python/python-virtual-environments-a-primer/)
* [LinkedIn Social Authentication in Django](https://realpython.com/blog/python/linkedin-social-authentication-in-django/)
* [Scaffold a Flask Project](https://realpython.com/blog/python/scaffold-a-flask-project/)
* [API Integration in Python - Part 1](https://realpython.com/blog/python/api-integration-in-python/)
* [Flask by Example - Updating the UI](https://realpython.com/blog/python/flask-by-example-updating-the-ui/)
* [Web Scraping and Crawling With Scrapy and MongoDB](https://realpython.com/blog/python/web-scraping-and-crawling-with-scrapy-and-mongodb/)
* [Web Scraping With Scrapy and MongoDB](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)
* [Setting Up a Simple OCR Server](https://realpython.com/blog/python/setting-up-a-simple-ocr-server/)
* [Handling Email Confirmation During Registration in Flask](https://realpython.com/blog/python/handling-email-confirmation-in-flask/)
* [Fingerprinting Images for Near-Duplicate Detection](https://realpython.com/blog/python/fingerprinting-images-for-near-duplicate-detection/)
* [Caching External API Requests](https://realpython.com/blog/python/caching-external-api-requests/)
* [Twitter Sentiment - Python, Docker, Elasticsearch, Kibana](https://realpython.com/blog/python/twitter-sentiment-python-docker-elasticsearch-kibana/)
* [Adding Social Authentication to Django](https://realpython.com/blog/python/adding-social-authentication-to-django/)
* [Kickstarting Flask on Ubuntu - Setup and Deployment](https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/)
* [Flask by Example - Implementing a Redis Task Queue](https://realpython.com/blog/python/flask-by-example-implementing-a-redis-task-queue/)
* [Flask by Example - Text Processing With Requests, BeautifulSoup, and NLTK](https://realpython.com/blog/python/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/)
* [Face Detection in Python Using a Webcam](https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/)
* [Face Recognition With Python, in Under 25 Lines of Code](https://realpython.com/blog/python/face-recognition-with-python/)
* [Discover Flask, Part 1 - Setting up a static site](https://realpython.com/blog/python/introduction-to-flask-part-1-setting-up-a-static-site/)
* [Discover Flask, Part 2 - Creating a login page](https://realpython.com/blog/python/introduction-to-flask-part-2-creating-a-login-page/)
* [Flask by Example - Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
* [Flask by Example - Project Setup](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/)
* [Using Flask-Login for User Management With Flask](https://realpython.com/blog/python/using-flask-login-for-user-management-with-flask/)
* [Primer on Jinja Templating](https://realpython.com/blog/python/primer-on-jinja-templating/)
* [Primer on Python Decorators](https://realpython.com/blog/python/primer-on-python-decorators/)
* [Python Web Applications With Flask - Part I](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/#.Uu6GOHddUp8)
* [Python Web Applications With Flask - Part II](https://realpython.com/blog/python/python-web-applications-with-flask-part-ii/#.Uu5-EHddUp8)
* [Python Web Applications With Flask - Part III](https://realpython.com/blog/python/python-web-applications-with-flask-part-iii/)
* [Getting Started With Bootstrap 3](https://realpython.com/blog/python/getting-started-with-bootstrap-3/)
* [Headless Selenium Testing With Python and PhantomJS](https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/)