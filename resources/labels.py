import json

from flask import jsonify
from flask_restful import Resource

from models import Label


class LabelListAPI(Resource):
    def get(self):
        labels = Label.objects()
        return jsonify(labels)
