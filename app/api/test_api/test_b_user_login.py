import  unittest
from app.api.v1 import  application
import json

data =""

class testUserLogin(unittest.TestCase):
    def setUp(self):
        self.app= application.test_client()
        self.url_prefix =""
        global data

    def test_a_with_invalid_json(self):
        global  data
        response = self.app.post("/login", data=data , headers={"Content-Type":"application/json"}, )
        self.assertEqual(response.status_code,200,"correct response status code")
        self.assertEqual(json.loads(response.get_data().decode())["error"],'this route required proper formated json ',"correct error message")
        data={}

    def test_b_with_no_data(self):
        response = self.app.post("/login", data=json.dumps(data), headers={"Content-Type": "application/json"}, )
        self.assertEqual(response.status_code, 200, "correct response status code")
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'password has not been provided',
                         "correct error message")
        data["password"]=1

    def test_c_with_incorrect_password(self):
        response = self.app.post("/login", data=json.dumps(data), headers={"Content-Type": "application/json"}, )
        self.assertEqual(response.status_code, 200, "correct response status code")
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'invalid login information',
                         "correct error message")


