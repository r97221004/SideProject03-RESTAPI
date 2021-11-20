from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT
import click


db = SQLAlchemy()

from Hotel.model.user import UserModel
from Hotel.model.tweet import TweetModel
from Hotel.model.style import StyleModel
from Hotel.model.room import RoomModel
from Hotel.resource.tweet import Tweet, TweetList
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
    api.add_resource(TweetList, "/tweets")

    register_commands(app)
    
    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--username', prompt = True, help = 'The username used to login.')
    @click.option('--password', prompt = True, hide_input = True, confirmation_prompt = True, help = 'The password used to login.')
    @click.option('--email', prompt = True, help = 'The email is required.')
    def admin(username, password, email):
        try:
            user = UserModel.get_by_username(username)    
            if user is not None: # 在這裡沒辦法寫 if user:
                click.echo("username already exists.")
            else:
                admin = UserModel.query.filter(UserModel.from_admin == True).first()
                if admin: # 如果數據庫中已經有管理員記錄就更新用戶名和密碼
                    click.echo('The administrator already exists, updating...')
                    admin.username = username
                    admin.set_password(password)
                    admin.email = email
                else: # 否則創建新的管理員記錄
                    click.echo('Creating the temporary administrator account...')
                    admin =UserModel(username = username, email = email, from_admin = True)
                    admin.set_password(password)
                    db.session.add(admin)
                db.session.commit()
                click.echo('Done.')
        except:
            click.echo('Database connection failed.')






