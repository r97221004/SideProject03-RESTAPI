from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from Hotel.model.room import RoomModel
from Hotel.model.style import StyleModel
from Hotel.model.user import UserModel


class RoomList(Resource):
    def get(self):
        rooms = RoomModel.get_room_list()
        return [room.as_dict() for room in rooms]


class RoomStyleList(Resource):
    def get(self, stylename):
        style = StyleModel.get_by_name(stylename)
        if not style:
            return {"message" : "style noy found."}, 404
        rooms = style.rooms
        return [room.as_dict() for room in rooms]
    
    @jwt_required()
    def post(self, stylename):
        if current_identity.from_admin == False:
            return {"message": "Please use the right token."}

        parser = reqparse.RequestParser()
        parser.add_argument("name", type = str, help = "name is required", required = True)
        parser.add_argument("roomtype", type = str, help = "roomtype is required", required = True)
        parser.add_argument("price", type = int, help = "price is required", required = True)
        data = parser.parse_args()

        room = RoomModel.get_by_name(data['name'])
        if room:
            return {"message": "room exists"}

        style = StyleModel.get_by_name(stylename)
        if not style:
            return {"message" : "style noy found."}, 404
        room = RoomModel(name = data["name"], roomtype = data['roomtype'], price = data['price'], style_id = style.id)
        room.add()
        return room.as_dict(), 201


class Room(Resource):
    def get(self, roomname):
        room = RoomModel.get_by_name(roomname)
        if not room:
            return {"message": "room not found."}
        return room.as_dict()

    @jwt_required()
    def patch(self, roomname):
        if current_identity.from_admin == False:
            return {"message": "Please use the right token."}

        parser = reqparse.RequestParser()
        parser.add_argument("roomtype", type = str)
        parser.add_argument("price", type = int)
        parser.add_argument("user_id_now", type = int)
        data = parser.parse_args()

        room = RoomModel.get_by_name(roomname)
        if not room:
            return {"message": "room not found."}

        if data['roomtype']:
            room.roomtype = data['roomtype']
        if data['price']:
            room.price = data['price']
        if data['user_id_now']:
            if data['user_id_now'] == -1:
                room.user_id_now = None
            elif not UserModel.get_by_id(data['user_id_now']):
                return {"message":"the user ID not found."}
            else:
                room.user_id_now = data["user_id_now"]

        room.update()
        return room.as_dict()

    @jwt_required()
    def delete(self, roomname):
        if current_identity.from_admin == False:
            return {"message": "Please use the right token."}
        
        room = RoomModel.get_by_name(roomname)
        if not room:
            return {"message": "room not found."}
        room.delete()
        return "", 204

