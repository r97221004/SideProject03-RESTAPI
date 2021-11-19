from Hotel import db


class Base(db.Model):

    __abstract__ = True # 這樣才不會被當成一個 table

    def as_dict(self):
        return { c.name:getattr(self, c.name) for c in self.__table__.columns}

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()