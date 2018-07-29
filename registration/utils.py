from datetime import datetime, timedelta
import bcrypt
import uuid

def get_expiry_date():
    now = datetime.utcnow().replace(second=0, microsecond=0)
    return now + timedelta(days=30)

def hash_password(clear_password):
    salt = bcrypt.gensalt(14)
    hashed_password = bcrypt.hashpw(clear_password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def generate_token():
    return str(uuid.uuid4())