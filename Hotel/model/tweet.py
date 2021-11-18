from datetime import datetime, tzinfo
from dateutil import tz
from dateutil.tz import tzlocal
from Hotel import db


# get local time zone name
tz_name = datetime.now(tzlocal()).tzname()  # 當地的時區名字
from_zone = tz.gettz('UTC') # UTC 時區
to_zone = tz.gettz(tz_name) # 當地時區


class TweetModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_model.id')) # 記住後面的寫法, 要的是 table 的名字, 不是 Class
    body = db.Column(db.String(140))
    created_at = db.Column(db.DateTime, default = datetime.utcnow, index = True)
    user = db.relationship('UserModel', back_populates = "tweets")

    def __repr__(self):
        return f"user_id: {self.user_id}, tweet: {self.body}"

    def as_dict(self):
        t = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        t['created_at'] = t['created_at'].replace(tzinfo = from_zone) # 告訴 datetime object 這是 UTC 時區
        t['created_at'] = t['created_at'].astimezone(to_zone) # 轉成當地時區
        t['created_at'] = t['created_at'].isoformat()  # 要加這個時間才會被序列化, 會把 datetime 類型轉乘字串
        return t
    
    def add(self):
        db.session.add(self)
        db.session.commit()