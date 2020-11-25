from flask import Flask
from flask_restful import Api

from api.models import db
from api import views

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = '{}://{}:{}@{}/{}'.format(
    'postgresql+psycopg2', 'root', 'secret', 'sqldb', 'postgres')

db.init_app(app)

api.add_resource(views.RequestView, '/request', '/request/<book_id>')
