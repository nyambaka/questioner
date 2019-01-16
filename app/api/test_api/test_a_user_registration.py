import unittest
from app import create_app
import json
from ..v1.utils.error_file import en_errors

application = create_app()

data = ""


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        self.url_prefix = "api/v1"
        self.app = application.test_client()

    def test_a_signup_with_wrong_data_format(self):
        global data
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"}, data="")
        self.assertEqual(response.status_code, 400, "wrong data format for this route use json")
        result = json.loads(response.get_data().decode())
        self.assertEqual(result, {'error': 'this route required proper formated json ', 'status': 400}
                         ,
                         "correct error message should be given back")
        data = {}

    def tst_zone(self):
        response = self.app.post(self.url_prefix + "/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(data))
        return response

    def assert_master(self, response, error_code):
        self.assertEqual(json.loads(response.get_data().decode())["error"], en_errors[error_code],
                         en_errors[error_code])

    def test_b_test_signup_with_password_missing(self):
        response = self.tst_zone()
        self.assert_master(response, 403)
        self.data = {"password": 1}

    def test_c_test_signup_with_no_first_name(self):
        response = self.tst_zone()
        self.assert_master(response, 403)
        data["firstname"] = 4

    def test_d_with_in_correct_first_name(self):
        response = self.tst_zone()
        self.assert_master(response, 404)
        data["firstname"] = "nelson"

    def test_e_with_last_name(self):
        response = self.tst_zone()
        self.assert_master(response, 405)
        data["lastname"] = 1

    def test_f_with_incorrect_last_name(self):
        response = self.tst_zone()
        self.assert_master(response, 406)
        data["lastname"] = "nyambaka"

    def test_g_with_no_othername(self):
        response = self.tst_zone()
        self.assert_master(response, 407)
        data["othername"] = 8

    def test_h_with_incorrect_othername(self):
        response = self.tst_zone()
        self.assert_master(response, 408)
        data["othername"] = "nyambaka"

    def test_i_with_no_email(self):
        response = self.tst_zone()
        self.assert_master(response, 409)
        data["email"] = 1

    def test_j_with_incorrect_email(self):
        response = self.tst_zone()
        self.assert_master(response, 410)
        data["email"] = "nelsonnyambaka@gmail.com"

    def test_k_with_no_phone_number(self):
        response = self.tst_zone()
        self.assert_master(response, 411)
        data["phonenumber"] = 4

    def test_l_with_incorrect_phone_number(self):
        response = self.tst_zone()
        self.assert_master(response, 412)
        data["phonenumber"] = "+254700741837"

    def test_m_with_no_username(self):
        response = self.tst_zone()
        self.assert_master(response, 413)
        data["username"] = "gadafi"

    def test_n_with_registered_date(self):
        response = self.tst_zone()
        self.assert_master(response, 415)
        data["registered"] = "now"

    def test_o_with_no_registered(self):
        response = self.tst_zone()
        self.assert_master(response, 417)
        data["isadmin"] = 5

    def test_p_with_no_password(self):
        response = self.tst_zone()
        self.assert_master(response, 419)
        data["password"] = "nelsomking"
