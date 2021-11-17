
from flask_restful import Resource, reqparse
from Hotel.model.user import UserModel

class Login(Resource): 
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type = str, help = "username is required", required = True)
        parser.add_argument("password", type = str, help = "password is required", required = True)
        data = parser.parse_args()
        user = UserModel.query.filter(UserModel.username == data["username"]).first()
        if user:
            if not user.check_password(data["password"]):
                return {
                    "message": "login failed, please input the right username or password."
                }
            return{
                "message": "login success.",
                "token": user.generate_token()
            }
        return {
            "message": "login failed, please input the right username or password."
        }
