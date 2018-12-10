from source.db import db
from passlib.hash import pbkdf2_sha256 as sha256


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(15))
    password = db.Column(db.String(20))
    is_admin = db.Column(db.BOOLEAN)

    def __init__(self, uid, password, is_admin):
        self.uid = uid
        self.password = password
        self.is_admin = is_admin

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_uid(cls, uid):
        return cls.query.filter_by(uid=uid).first()

    @classmethod
    def find_by_admin(cls, uid):
        return cls.query.filter_by(uid=uid, is_admin=1).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
