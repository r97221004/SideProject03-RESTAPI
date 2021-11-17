from flask import current_app
from datetime import datetime, timedelta
from Hotel import db
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64))

    def __repr__(self):
        return f"id: {self.id}, username: {self.username}"

    def as_dict(self):
        return { c.name:getattr(self, c.name) for c in self.__table__.columns}

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_token(self):
        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes = 5),
                'iat': datetime.utcnow(),
                'sub': self.username
            }
            # create the string token using the payload and the SECRET key
            jwt_token = jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm = "HS256"
            )

            return jwt_token
        except Exception as e:
            # return an error
            return str(e)
