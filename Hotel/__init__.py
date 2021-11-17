from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()
from Hotel.resource.user import User, UserList


def create_app():
    app = Flask("Hotel")    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Aa137540@localhost:3306/demo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app)
    migrate = Migrate(app, db)
    db.init_app(app)


    api.add_resource(UserList, "/users")
    api.add_resource(User, "/user/<string:username>")

    return app