import unittest
from app import create_app
import json

application = create_app()


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        self.url_prefix = "api/v1"
        self.app = application.test_client()
        self.data = {
            "firstname": "nelson",
            "lastname": "nyambaka",
            "othername": "nyambaka",
            "email": "nelsonnyambaka@gmail.com",
            "phonenumber": "0700741837",
            "username": "nelly",
            "registered": "2018-01-20",
            "isadmin": 1,
            "password": "nelsonking"
        }

    def test_a_user_register(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(self.data))
        result = json.loads(response.get_data().decode())
        self.assertEqual(result["data"]["firstname"], "nelson", "first name should be correct")
        self.assertEqual(result["data"]["lastname"], "nyambaka", "last name should be correct")
        self.assertEqual(result["data"]["othername"], "nyambaka", "other name should be correct")
        self.assertEqual(result["data"]["email"], "nelsonnyambaka@gmail.com", "email should be correct")
        self.assertEqual(result["data"]["phonenumber"], "0700741837", "phonenumber should be correct")
        self.assertEqual(result["data"]["username"], "nelly", "phonenumber should be correct")
        self.assertEqual(result["data"]["registered"], "2018-01-20", "registered should be correct")
        self.assertEqual(result["data"]["isadmin"], 1, "isadmin should be correct")
        self.assertEqual(result["data"]["password"], "nelsonking", "password should be correct")
        self.assertEqual(response.status_code, 201, "user created successfully")

    def test_b_user_login(self):
        response = self.app.post(self.url_prefix + "/login", headers={"Content-Type": "application/json"},
                                 data=json.dumps(self.data))
        result = json.loads(response.get_data().decode())
        self.assertEqual(result["data"]["firstname"],"nelson","correct firstname should be returned")
        self.assertEqual(response.status_code, 201, "correct status code should be returned")