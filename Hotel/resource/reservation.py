from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from Hotel.model.room import RoomModel
from Hotel.model.user import UserModel


class Reservation(Resource):
    @jwt_required()
    def get(self, username):
        if current_identity.username != username:
            return {"message": "Please use the right token."}
        
        user = UserModel.get_by_username(username)
        rooms = RoomModel.get_by_user_id(user.id)
        return [room.as_dict() for room in rooms]


    @jwt_required()
    def put(self, username):
        if current_identity.username != username:
            return {"message": "Please use the right token."}
        
        parser = reqparse.RequestParser()
        parser.add_argument("name", type = str, help = "name is required.", required = True)
        data = parser.parse_args()

        room = RoomModel.get_by_name(data["name"])
        if not room:
            return {"message": "room not found."}
        if room.user_id_now:
            return {"message": "The room is not available."}
        
        user = UserModel.get_by_username(username)
        room.user_id_now = user.id
        room.update()
        return {"message": "Your Booking Is Confirmed."}

    
    @jwt_required()
    def delete(self, username):
        if current_identity.username != username:
            return {"message": "Please use the right token."}

        user = UserModel.get_by_username(username)
        rooms = RoomModel.get_by_user_id(user.id)
        for room in rooms:
            room.user_id_now = None
            room.update()
        
        return {"message": "Cancel the reservation."}