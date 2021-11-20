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


    