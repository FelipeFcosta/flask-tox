from flask import Flask, jsonify
from flask_cors import CORS


def create_app(config=None):
    app = Flask(__name__)


    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})


    CORS(app)

    @app.route("/")
    def hello_world():
        return "Hello World"

    @app.route("/foo/<someId>")
    def foo_url_arg(someId):
        return jsonify({"echo": someId})

    return app