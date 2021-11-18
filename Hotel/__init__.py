from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT


db = SQLAlchemy()

from Hotel.model.user import UserModel
from Hotel.model.tweet import TweetModel
from Hotel.resource.tweet import Tweet
from Hotel.resource.user import User, UserList
from Hotel.config import Config

jwt = JWT(None, UserModel.authenticate, UserModel.identity)

def create_app():
    app = Flask("Hotel")   
    app.config.from_object(Config)
    api = Api(app)
    migrate = Migrate(app, db)
    db.init_app(app)
    jwt.init_app(app)

    api.add_resource(UserList, "/users")
    api.add_resource(User, "/user/<string:username>")
    api.add_resource(Tweet, "/tweets/<string:username>")
    
    return app