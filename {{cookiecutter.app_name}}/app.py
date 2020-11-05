from flask import Flask
from flask_restx import Api

from .routes import indexRouter

app = Flask(__name__)

api = Api(
    title="test",
    version="0.1.0"
)


api.add_namespace(indexRouter, "/")

api.init_app(app)