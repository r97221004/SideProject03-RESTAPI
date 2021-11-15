from flask import Flask, jsonify, request


app = Flask(__name__)

user_list = [
    {"username": "Matt", "password": "123"},
    {"username": "Crystal", "password": "456"}
]



@app.route('/')
def index():
    return "Hello, World!"


@app.route('/users', methods = ['GET', 'POST'])
def get_users():
    if request.method == "POST":
        user = request.get_json()
        user_check = list(filter(lambda x: x['username'] == user['username'], user_list))
        if not user_check: 
            user_list.append(user)
            return {"message": "user created."}, 201
        else:
            return {"message": "user exists."}

    return jsonify(user_list)


@app.route("/user/<string:username>", methods = ["DELETE", "PUT"])
def delete_user(username):
    user_find = None
    for user in user_list:
        if user['username'] == username:
            user_find = user

    if not user_find:
        return {"message":"user not found" }

    
    if request.method == "DELETE":
        user_list.remove(user_find)
        return {"message": "user deleted"}
    
    elif request.method == "PUT":
        user_list.remove(user_find)
        user_list.append({
            "username": username,
            "password": request.get_json()["password"]
        })

        return {"message": "user password updated"}





