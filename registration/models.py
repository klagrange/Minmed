import datetime
from application import db, Base
from sqlalchemy.schema import Sequence

class UserMaster(Base):
    __tablename__ = 'user_master'

    id = db.Column(db.Integer, Sequence('id'), primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    saving_amount = db.Column(db.Integer(), nullable=False)
    loan_amount = db.Column(db.Integer(), nullable=False)
    access = db.relationship('Access', backref='user_master', uselist=False)

    def __init__(self, username, password, saving_amount, loan_amount, access):
        self.username = username
        self.password = password
        self.saving_amount = saving_amount
        self.loan_amount = loan_amount
        self.access = access

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Access(Base):
    __tablename__ = 'access'

    id = db.Column(db.Integer, Sequence('id'), primary_key=True)
    user_master_id = db.Column(db.Integer, db.ForeignKey('user_master.id'), nullable=False)
    token = db.Column(db.String(), nullable=False)
    expires = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, token, expires):
        self.token = token
        self.expires = expires

    def __repr__(self):
        return '<id {}>'.format(self.id)

