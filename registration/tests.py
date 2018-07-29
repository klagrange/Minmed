import unittest
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from application import Base
from application import create_app as create_app_base
from settings import SQLALCHEMY_DATABASE_URI_TEST
from registration.models import UserMaster, Access
from registration.logic import get_user_profile

class RegistrationTest(unittest.TestCase):

    def create_app(self):
        return create_app_base(SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI_TEST)

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()

        engine = create_engine(SQLALCHEMY_DATABASE_URI_TEST, convert_unicode=True)
        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                                 autoflush=False,
                                                 bind=engine))
    def tearDown(self):
        pass

    def register_dict(self, 
        username="username",
        password="password",
        saving_amount=0,
        loan_amount=0):
        return json.dumps(dict(
                username=username,
                password=password,
                savingAmount=saving_amount,
                loanAmount=loan_amount
                ))
    
    def access_dict(self, username, password):
        return json.dumps(dict(
            username=username,
            password=password
        ))

    def register(self, data):
        return self.app.post('/register', 
                             data=data,
                             content_type="application/json")

    def get_access(self, data):
        return self.app.post('/register/access_token',
                             data=data,
                             content_type="application/json")

    def test_register(self):
        # register a user
        rv = self.register(data=self.register_dict())
        assert rv.status_code == 200

        # register a user with wrong or missing params
        rv = self.register(data=json.dumps(dict(
            username="username"
        )))
        assert rv.status_code == 400

        rv = self.register(data=json.dumps(dict(
            username="username",
            password="password",
            savingAmount=0
        )))
        assert rv.status_code == 400

        # register the same user
        rv = self.register(data=self.register_dict())
        assert rv.status_code == 400

class ProfileLogicTest(unittest.TestCase):

    def test_logic(self):
        assert get_user_profile(0, 10000) == "D"
        assert get_user_profile(2000, 10000) == "D"
        assert get_user_profile(4000, 10000) == "C"
        assert get_user_profile(10000, 0) == "A"
        

if __name__ == '__main__':
    unittest.main()
