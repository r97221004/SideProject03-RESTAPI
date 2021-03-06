from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT
import click


db = SQLAlchemy()
migrate = Migrate()

from Hotel.model.user import UserModel
from Hotel.resource.tweet import Tweet, TweetList
from Hotel.resource.user import User, UserList
from Hotel.resource.style import StyleList
from Hotel.resource.room import RoomStyleList, RoomList, Room
from Hotel.resource.reservation import Reservation
from Hotel.resource.home import Home
from Hotel.config import app_config

jwt = JWT(None, UserModel.authenticate, UserModel.identity)


def create_app(config_name="development"):
    app = Flask("Hotel")
    app.config.from_object(app_config[config_name])
    api = Api(app)
    migrate.init_app(app, db)
    db.init_app(app)
    jwt.init_app(app)

    api.add_resource(UserList, "/users")
    api.add_resource(User, "/user/<string:username>")
    api.add_resource(Tweet, "/tweets/<string:username>")
    api.add_resource(TweetList, "/tweets")
    api.add_resource(StyleList, "/styles")
    api.add_resource(RoomList, "/rooms")
    api.add_resource(RoomStyleList, "/rooms/<string:stylename>")
    api.add_resource(Room, "/room/<string:roomname>")
    api.add_resource(Reservation, "/reservation/<string:username>")
    api.add_resource(Home, "/")

    register_commands(app)

    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.option('--password', prompt=True,
                  hide_input=True, confirmation_prompt=True, help='The password used to login.')
    @click.option('--email', prompt=True, help='The email is required.')
    def admin(username, password, email):
        try:
            user = UserModel.get_by_username(username)
            if user is not None:  # 在這裡沒辦法寫 if user:
                click.echo("username already exists.")
            else:
                admin = UserModel.query.filter(UserModel.from_admin is True).first()
                if admin:  # 如果數據庫中已經有管理員記錄就更新用戶名和密碼
                    click.echo('The administrator already exists, updating...')
                    admin.username = username
                    admin.set_password(password)
                    admin.email = email
                else:  # 否則創建新的管理員記錄
                    click.echo('Creating the temporary administrator account...')
                    admin = UserModel(username=username, email=email, from_admin=True)
                    admin.set_password(password)
                    db.session.add(admin)
                db.session.commit()
                click.echo('Done.')
        except:
            click.echo('Database connection failed.')
