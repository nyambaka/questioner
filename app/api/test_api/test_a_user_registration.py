import  unittest
from app.api.v1 import  application
import json

data=""

class TestUserLogin(unittest.TestCase):

    def setUp(self):

        self.url_prefix=""
        self.app = application.test_client()

    def test_a_signup_with_wrong_data(self):
        global data
        response = self.app.post(self.url_prefix+"/signup",headers ={"Content-Type":"application/json"},data = "")
        self.assertEqual(response.status_code,200,"signup method is allowed")
        self.assertEqual(json.loads(response.get_data().decode()),{'error': 'this route required proper formated json '},"correct error message should be given back")
        data = {}

    def test_b_test_signup_with_password_missing(self):
        response = self.app.post(self.url_prefix+"/signup",headers={"Content-Type":"application/json"},data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"],'first name has not been set',"password missing error shoulb be noted")
        self.data = {"password":1}

    def test_c_test_signup_with_no_first_name(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'first name has not been set',
                         "password missing error shoulb be noted")
        data["firstname"] = 4

    def test_d_with_in_correct_first_name(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'first name should be of type string',
                         "password missing error shoulb be noted")
        data["firstname"] = "nelson"

    def test_e_with_last_name(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'last name has not been set',
                         "password missing error shoulb be noted")
        data["lastname"] = 1

    def test_f_with_incorrect_last_name(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'last name should be of type string',
                         "password missing error shoulb be noted")
        data["lastname"] = "nyambaka"

    def test_g_with_no_othername(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'other-name has not been given',
                         "test_g_with_no_othername")
        data["othername"] = 8

    def test_h_with_incorrect_othername(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'other name should be of type string',
                         "test_h_with_incorrect_othername")
        data["othername"] = "nyambaka"

    def test_i_with_no_email(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'email has not been provided',
                         "test_h_with_incorrect_othername")
        data["email"] = 1

    def test_j_with_incorrect_email(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'email should be of type string',
                         "test_h_with_incorrect_othername")
        data["email"] = "nelsonnyambaka@gmail.com"

    def test_k_with_no(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'phoneNumber has not been provided',
                         "test_h_with_incorrect_othername")
        data["phonenumber"] = 4

    def test_l_with_incorrect_phone_number(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'phoneNumber should be of type string',
                         "test_h_with_incorrect_othername")
        data["phonenumber"] = "+254700741837"

    def test_m_with_no_username(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'username has not been provided',
                         "test_h_with_incorrect_othername")
        data["username"] = "gadafi"

    def test_n_with_registered_date(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'registered has not been provided',
                         "test_h_with_incorrect_othername")
        data["registered"] = "now"

    def test_o_with_no_registered(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'is admin has not been provided',
                         "test_h_with_incorrect_othername")
        data["isadmin"] =5

    def test_p_with_no_password(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        self.assertEqual(json.loads(response.get_data().decode())["error"], 'password has not been provided',
                         "test_h_with_incorrect_othername")
        data["password"] ="nelsomking"
