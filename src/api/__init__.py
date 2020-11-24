from flask import Flask
from flask_restful import Api
from api.models import db
from api import views


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    'root', 'secret', 'sqldb', 'postgres')

db.init_app(app)

api.add_resource(views.HelloWorld, '/')
