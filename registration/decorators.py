from functools import wraps
from flask import request, jsonify
import datetime

from .models import UserMaster, Access

def app_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = request.headers.get('X-APP-ID')
        user_token = request.headers.get('X-APP-TOKEN')

        if user_id is None or user_token is None:
            return jsonify({"error": "provide custom auth headers"}), 403

        user = UserMaster.query.filter_by(username=user_id).first()
        if not user:
            return jsonify({"error": "NOT_FOUND"}), 403

        access = user.access
        if access.token != user_token:
            return jsonify({"error": "WRONG_TOKEN"}), 403
        if access.expires < datetime.datetime.utcnow():
            return jsonify({"error": "TOKEN_EXPIRED"}), 403

        return f(*args, **kwargs)
    return decorated_function
