import os
import json
from flask import Flask
from flask_cors import CORS

HTTP_OK = 200

from importlib.metadata import version
try:
    __version__ = version(__name__)
except:
    __version__ = "dev"

def create_app():
    app = Flask(__name__)

    cors = CORS(app)

    @app.route('/status/alive', methods=['GET'])
    def alive():
        data = {
            'status': 'Greeter service is alive',
        }

        return app.response_class(
            response=json.dumps(data),
            status=HTTP_OK,
            mimetype='application/json',
        )

    @app.route('/status/healthy', methods=['GET'])
    def healthy():
        data = {
            'status': 'Greeter service is healthy',
        }

        return app.response_class(
            response=json.dumps(data),
            status=HTTP_OK,
            mimetype='application/json',
        )

    @app.route('/', methods=['GET'])
    def index():
        data = {
            'greeting': 'hello',
        }

        return app.response_class(
            response=json.dumps(data),
            status=HTTP_OK,
            mimetype='application/json',
        )

    @app.after_request
    def after_request_func(response):
        response.headers['X-Reply-Service']='greeter-service'
        response.headers['X-Version']='15679299999'
        return response

    return app
