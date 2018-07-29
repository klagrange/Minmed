from flask import Blueprint
from .api import RegistrationAPI, AccessAPI
# from application import db_session

def attach_db_session(db_session):
    registration_app = Blueprint('registration_app', __name__)

    registration_view = RegistrationAPI.as_view('registration_api', db_session)
    registration_app.add_url_rule('/register', view_func=registration_view, methods=['POST',])

    access_view = AccessAPI.as_view('access_api', db_session)
    registration_app.add_url_rule('/register/access_token', view_func=access_view, methods=['POST',])

    return registration_app