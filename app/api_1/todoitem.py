#!/usr/bin/env python
#coding=utf-8
from flask_restful import Api, Resource, url_for

class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}