import  unittest
from app import  create_app
import json

application =create_app()
data =""

class testUserLogin(unittest.TestCase):
    def setUp(self):
        self.app= application.test_client()
        self.url_prefix ="api/v1"
        global data

    def test_a_with_invalid_json(self):
        global  data
        response = self.app.post(self.url_prefix+"/login", data=data , headers={"Content-Type":"application/json"}, )
        self.assertEqual(json.loads(response.get_data().decode())["error"],'this route required proper formated json ',"correct error message")
        data={}

    def test_b_with_no_data(self):
        response = self.app.post(self.url_prefix+"/login", data=json.dumps(data), headers={"Content-Type": "application/json"}, )
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'password has not been provided',
                         "correct error message")
        data["password"]=1

    def test_c_with_incorrect_password(self):
        response = self.app.post(self.url_prefix+"/login", data=json.dumps(data), headers={"Content-Type": "application/json"}, )
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'invalid login information',
                         "correct error message")


