import unittest
from app import create_app
import json
from ..v1.utils.error_file import en_errors

application =create_app()

data = ""


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        self.url_prefix = "api/v1"
        self.app = application.test_client()

    def test_a_signup_with_wrong_data(self):
        global data
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"}, data="")
        self.assertEqual(response.status_code, 400, "signup method is allowed")
        self.assertEqual(json.loads(response.get_data().decode()),{'error': 'this route required proper formated json ', 'status': 400}
                        ,
                         "correct error message should be given back")
        data = {}

    def tst_zone(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        return response

    def assert_master(self, response, error_code, message):
        self.assertEqual(json.loads(response.get_data().decode())["error"], en_errors[error_code], message)

    def test_b_test_signup_with_password_missing(self):
        response= self.tst_zone()
        self.assert_master(response, 403,"password missing error shoulb be noted")
        self.data = {"password": 1}

    def test_c_test_signup_with_no_first_name(self):
        response= self.tst_zone()
        self.assert_master(response, 403, "password missing error shoulb be noted")
        data["firstname"] = 4

    def test_d_with_in_correct_first_name(self):
        response= self.tst_zone()
        self.assert_master(response, 404, "password missing error shoulb be noted")
        data["firstname"] = "nelson"

    def test_e_with_last_name(self):
        response= self.tst_zone()
        self.assert_master(response, 405, "password missing error shoulb be noted")
        data["lastname"] = 1

    def test_f_with_incorrect_last_name(self):
        response= self.tst_zone()
        self.assert_master(response, 406, "password missing error shoulb be noted")
        data["lastname"] = "nyambaka"

    def test_g_with_no_othername(self):
        response= self.tst_zone()
        self.assert_master(response, 407, "test_g_with_no_othername")
        data["othername"] = 8

    def test_h_with_incorrect_othername(self):
        response= self.tst_zone()
        self.assert_master(response, 408, "test_h_with_incorrect_othername")
        data["othername"] = "nyambaka"

    def test_i_with_no_email(self):
        response= self.tst_zone()
        self.assert_master(response, 409, "test_h_with_incorrect_othername")
        data["email"] = 1

    def test_j_with_incorrect_email(self):
        response= self.tst_zone()
        self.assert_master(response, 410, "test_h_with_incorrect_othername")
        data["email"] = "nelsonnyambaka@gmail.com"

    def test_k_with_no(self):
        response= self.tst_zone()
        self.assert_master(response, 411, "test_h_with_incorrect_othername")
        data["phonenumber"] = 4

    def test_l_with_incorrect_phone_number(self):
        response= self.tst_zone()
        self.assert_master(response, 412, "test_h_with_incorrect_othername")
        data["phonenumber"] = "+254700741837"

    def test_m_with_no_username(self):
        response= self.tst_zone()
        self.assert_master(response, 413, "test_h_with_incorrect_othername")
        data["username"] = "gadafi"

    def test_n_with_registered_date(self):
        response= self.tst_zone()
        self.assert_master(response, 415, "test_h_with_incorrect_othername")
        data["registered"] = "now"

    def test_o_with_no_registered(self):
        response= self.tst_zone()
        self.assert_master(response, 417, "test_h_with_incorrect_othername")
        data["isadmin"] = 5

    def test_p_with_no_password(self):
        response= self.tst_zone()
        self.assert_master(response, 419, "test_h_with_incorrect_othername")
        data["password"] = "nelsomking"
