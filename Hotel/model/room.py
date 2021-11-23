from Hotel import db
from Hotel.model.base import Base


class RoomModel(Base):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    roomtype = db.Column(db.String(64))
    price = db.Column(db.Integer)
    style_id = db.Column(db.Integer, db.ForeignKey('style_model.id'))
    user_id_now = db.Column(db.Integer, db.ForeignKey('user_model.id'))

    style = db.relationship("StyleModel", back_populates = "rooms")
    user = db.relationship("UserModel", back_populates = "rooms")

    @staticmethod
    def get_room_list():
        return RoomModel.query.all()

    @staticmethod
    def get_by_name(name):
        return RoomModel.query.filter(RoomModel.name == name).first()
        

    @staticmethod
    def get_by_user_id(id):
        return RoomModel.query.filter(RoomModel.user_id_now == id).all()
        

    