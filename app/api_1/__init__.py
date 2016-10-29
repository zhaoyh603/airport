from flask import Blueprint
from flask_restful import Api, Resource, url_for
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

from .todoitem import TodoItem
api.add_resource(TodoItem, '/todos/<int:id>')

