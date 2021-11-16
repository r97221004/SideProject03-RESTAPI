from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
app = Flask(__name__)
api = Api(app)

user_list = [
    {"username": "Crystal", "password": "123", "email": "crystal@gmail.com"},
    {"username": "Matt", "password": "456", "email": "matt@gmail.com"}
]


class UserList(Resource):
    def get(self):
        return user_list

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type = str, help = "username is required.", required = True)
        parser.add_argument("password", type = str, help = "password is required", required = True)
        parser.add_argument("email", type = str, help = "email is required", required = True)
        data = parser.parse_args()

        user_find = None
        for user in user_list:
            if user["username"] == data["username"]:
                user_find = user
                break
        
        if not user_find:
            user_list.append({
                "username": data["username"],
                "password": data["password"],
                "email": data["email"]
            })
            return user_list[-1], 201
        else:
            abort(409, message = "username exists.")


class User(Resource):
    def get(self, username):
        user_find = None
        for user in user_list:
            if user["username"] == username:
                user_find = user
                break
        if not user_find:
            abort(404, message = "user not found")
        else:
            return user_find

    def put(self, username):
        parser = reqparse.RequestParser() 
        parser.add_argument("password", type = str, help = "password is required", required = True)
        parser.add_argument("email", type = str, help = "email is required", required = True)
        data = parser.parse_args()

        user_find = None
        for user in user_list:
            if user["username"] == username:
                user_find = user
                break
        
        if not user_find:
            user_list.append({
                "username": username,
                "password": data['password'],
                "email": data["email"]
            })
            return user_list[-1], 201
        else:
            idx = user_list.index(user_find)
            user_list[idx]["password"] = data["password"]
            user_list[idx]["email"] = data["email"]
            return user_list[idx]

    def patch(self, username):
        parser = reqparse.RequestParser() 
        parser.add_argument("password", type = str)
        parser.add_argument("email", type = str)
        data = parser.parse_args()

        user_find = None
        for user in user_list:
            if user["username"] == username:
                user_find = user
                break
        
        if not user_find:
            abort(404, message = "user not found")
        else:
            idx = user_list.index(user_find)
            if data['password']:
                user_list[idx]["password"] = data['password']
            elif data['email']:
                user_list[idx]['email'] = data['email']

            return user_list[idx]

    def delete(self, username):
        user_find = None
        for user in user_list:
            if user["username"] == username:
                user_find = user
                break
        if not user_find:
            abort(404, messsage = "user not found")
        else:
            user_list.remove(user_find)
            return "", 204



api.add_resource(UserList, "/users")
api.add_resource(User, "/user/<string:username>")