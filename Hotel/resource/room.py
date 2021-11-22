from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from Hotel.model.room import RoomModel
from Hotel.model.style import StyleModel




class RoomList(Resource):
    def get(self):
        rooms = RoomModel.get_room_list()
        return [room.as_dict() for room in rooms]


class Room(Resource):
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