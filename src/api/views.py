from flask_restful import Resource
from api.models import Book


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

