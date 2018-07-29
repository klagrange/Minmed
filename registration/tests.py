import unittest
import json

from application import create_app as create_app_base
from settings import SQLALCHEMY_DATABASE_URI_TEST


class PetTest(unittest.TestCase):

    def create_app(self):
        return create_app_base(SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI_TEST)

    def setUp(self):
        self.app = self.create_app()

    def tearDown(self):
        pass

    def app_dict(self):
        return json.dumps(dict(
                app_id="pet_client",
                app_secret="pet_secret"
                ))
    
    def test_xxx(self):
        print("YO!")

if __name__ == '__main__':
    unittest.main()
