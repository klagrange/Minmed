from flask.views import MethodView
from flask import jsonify, request, abort
from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match
from sqlalchemy import exists
from datetime import datetime, timedelta
import bcrypt
import uuid

# from application import db_session
from .schemas import register as schema_register
from .schemas import access as schema_access
from .models import UserMaster, Access
from .vos import user_vo, access_vo
from .utils import get_expiry_date, hash_password, generate_token

class RegistrationAPI(MethodView):

    def __init__(self, db_session):
        if not request.json:
            abort(400)

        self._db_session = db_session

    def post(self):        
        req = request.json

        # ensure correct schema
        error = best_match(Draft4Validator(schema_register).iter_errors(req))
        if error:
            return jsonify({"error": error.message}), 400
        
        # ensure that 'username' field is unique
        if self._db_session.query(exists().where(UserMaster.username == req.get('username'))).scalar():
            return jsonify({"error": 'username already exists'}), 400 
        
        # register new user & its profile
        user = UserMaster(
            username = req.get('username'),
            password = hash_password(req.get('password')),
            saving_amount = req.get('savingAmount'),
            loan_amount = req.get('loanAmount'),
            access = Access(generate_token(), get_expiry_date())
        )
        self._db_session.add(user)
        self._db_session.commit()

        return jsonify(user_vo(user)), 200

class AccessAPI(MethodView):

    def __init__(self, db_session):
        if not request.json:
            abort(400)
        self._db_session = db_session

    def post(self):
        req = request.json

        # ensure correctness of request schema
        error = best_match(Draft4Validator(schema_access).iter_errors(req))
        if error:
            return jsonify({
                "error": error.message,
                "expectedSchema": schema_access
                }), 400

        # ensure existance of provided username
        user = UserMaster.query.filter_by(username=req.get('username')).first()
        if not user:
            return jsonify({ "error": "incorrect credentials: username '{0}' does not exist".format(req.get('username')) }), 403
        
        # ensure correctness of password
        if not bcrypt.checkpw(req.get('password').encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({ "error": "incorrect password" }), 403

        # delete existing tokens
        Access.query.filter(Access.user_master_id == user.id).delete()
        self._db_session.commit()

        # generate token
        user.access = Access(generate_token(), get_expiry_date()) 
        self._db_session.commit()

        return jsonify(access_vo(user.access)), 200








