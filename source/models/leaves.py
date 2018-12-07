from source.db import db


class LeaveModel(db.Model):
    __tablename__ = 'leaves'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(15))
    l_type = db.Column(db.String(30))
    l_from = db.Column(db.String(10))
    l_to = db.Column(db.String(10))
    l_details = db.Column(db.String(100))
    l_status = db.Column(db.String(20))

    def __init__(self, uid, l_type, l_from,
                 l_to, l_details, l_status):
        self.uid = uid
        self.l_type = l_type
        self.l_from = l_from
        self.l_to = l_to
        self.l_details = l_details
        self.l_status = l_status

    def json(self):
        return {'uid': self.uid,
                'l_type': self.l_type,
                'l_from': self.l_from,
                'l_to': self.l_to,
                'l_details': self.l_details,
                'l_status': self.l_status}

    @classmethod
    def find_by_uid(cls, uid):
        return cls.query.filter_by(uid=uid).first()

    @classmethod
    def find_by_uid_all(cls, uid):
        return cls.query.filter_by(uid=uid)

    @classmethod
    def find_by_status(cls, uid):
        return cls.query.filter_by(uid=uid, l_status='pending approval').first()

    @classmethod
    def find_by_l_id(cls, l_id):
        return cls.query.filter_by(id=l_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()