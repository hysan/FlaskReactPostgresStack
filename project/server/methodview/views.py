# project/server/methodview/views.py


from flask import Blueprint, render_template
from flask.views import MethodView

methodview_blueprint = Blueprint('methodview', __name__)

class ExamplePage(MethodView):
    def get(self):
        return """
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/react@15.3.2/dist/react.js"></script>
  <script src="https://unpkg.com/react-dom@15.3.2/dist/react-dom.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.23/browser.min.js"></script>
  <style>
  </style>
</head>
<body>
  <div id="container">
  </div>
  <script type="text/babel">
    var destination = document.querySelector("#container");

    ReactDOM.render(
      <div>
        Hello World MethodView!
      </div>,
      destination
    );
  </script>
</body>
</html>
        """

class ExampleTemplatePage(MethodView):
    def get(self):
      return render_template('index.html')

static_view = ExamplePage.as_view('static_page')
templated_view = ExampleTemplatePage.as_view('templated_page')

methodview_blueprint.add_url_rule(
    '/static',
    view_func=static_view,
    methods=['GET']
)
methodview_blueprint.add_url_rule(
    '/template',
    view_func=templated_view,
    methods=['GET']
)