from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}


class HelloName(Resource):
    def get(self, name):
        return {"message": f"Hello, {name}!"}



api.add_resource(HelloWorld, "/helloworld")
api.add_resource(HelloName, "/helloname/<string:name>")