import json

import flask
from flask import Flask, request, redirect, url_for, jsonify
from flask import render_template
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
from models import Label
import geojson

from resources.label import LabelAPI
from resources.labels import LabelListAPI

app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'db',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)

api.add_resource(LabelAPI, '/annotation/api/v1.0/createlabel/', endpoint='createlabel')
api.add_resource(LabelListAPI, '/annotation/api/v1.0/labels', endpoint='labels')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
