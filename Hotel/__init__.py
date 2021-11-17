from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()
from Hotel.resource.user import User, UserList
from Hotel.config import Config
from Hotel.resource.auth import Login

def create_app():
    app = Flask("Hotel")   
    app.config.from_object(Config)
    api = Api(app)
    migrate = Migrate(app, db)
    db.init_app(app)


    api.add_resource(UserList, "/users")
    api.add_resource(User, "/user/<string:username>")
    api.add_resource(Login, "/auth/login")

    return app