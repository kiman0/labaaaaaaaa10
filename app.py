from database.db import execute_query
from flask import Flask

app = Flask(__name__)


@app.route('/<string:name>/<string:location>')
def index(name, location):
    return execute_query('insert', name, location)


@app.route('/<string:name>')
def fetch(name):
    return execute_query('select', name)