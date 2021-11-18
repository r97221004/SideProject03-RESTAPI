from flask_restful import Resource, reqparse, abort, request
from flask import current_app
from flask_jwt import jwt_required
from Hotel.model.user import UserModel 

user_list = [
    {"username": "Crystal", "password": "123", "email": "crystal@gmail.com"},
    {"username": "Matt", "password": "456", "email": "matt@gmail.com"}
]


class UserList(Resource):
    @jwt_required()
    def get(self):
        users = UserModel.get_user_list()
        return [ user.as_dict() for user in users]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type = str, help = "username is required.", required = True)
        parser.add_argument("password", type = str, help = "password is required", required = True)
        parser.add_argument("email", type = str, help = "email is required", required = True)
        data = parser.parse_args()

        user = UserModel.get_by_username(data["username"])
        if user:
            abort(409, message = "username exists.")
        user = UserModel(username = data["username"], email = data["email"])
        user.set_password(data["password"])
        user.add()
        return user.as_dict(), 201


class User(Resource):
    def get(self, username):
        user = UserModel.get_by_username(username)
        if user:
            return user.as_dict()
        return  abort(404, message = "user not found")


    def put(self, username):
        parser = reqparse.RequestParser() 
        parser.add_argument("password", type = str, help = "password is required", required = True)
        parser.add_argument("email", type = str, help = "email is required", required = True)
        data = parser.parse_args()

        user = UserModel.get_by_username(username)
        if user:
            user.set_password(data["password"])
            user.email = data["email"]
            user.update()
            return user.as_dict()
        user = UserModel(username = username,  email = data["email"])
        user.set_password(data["password"])
        user.add()
        return user.as_dict(), 201


    def patch(self, username):
        parser = reqparse.RequestParser() 
        parser.add_argument("password", type = str)
        parser.add_argument("email", type = str)
        data = parser.parse_args()

        user = UserModel.get_by_username(username)

        if not user:
            abort(404, message = "user not found")
        else:
            if data["password"]:
                user.set_password(data["password"])
            if data["email"]:
                user.email = data["email"]
            user.update()
            return user.as_dict()


    def delete(self, username):
        user = UserModel.get_by_username(username)
        if not user:
            abort(404, messsage = "user not found")
        else:
            user.delete()
            return "", 204
 

