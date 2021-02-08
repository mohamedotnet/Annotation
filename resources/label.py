from flask import request
from flask_restful import Resource
from models import Label


class LabelAPI(Resource):
    def post(self):
        label_object = request.get_json()
        label = Label(label=label_object['label'],
                      _type=label_object['type'],
                      geometry=label_object['geometry'],
                      properties=label_object['properties'],
                      style=label_object['style']
                      )
        label.save(validate=False)
        return label_object
