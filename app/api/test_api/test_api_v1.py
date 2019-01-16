import unittest
from app import create_app
from app.api.v1.utils.error_file import en_errors
import json

application = create_app()

data = ""


class TestMeetups(unittest.TestCase):

    def setUp(self):
        self.client = application.test_client()
        self.url_prefix = "api/v1"

    def test_a_post_meetup(self):
        global data
        response = self.client.post(self.url_prefix + "/meetups", headers={"Content-Type": "application/json"},
                                    data=data)
        self.assertEqual(json.loads(response.get_data().decode())["error"], en_errors[63],
                         en_errors[63])
        data = {}

    def tst_zone(self):
        response = self.client.post(self.url_prefix + "/meetups", headers={"Content-Type": "application/json"},
                                    data=json.dumps(data))
        return response

    def asset_master(self, response, error_code):
        self.assertEqual(json.loads(response.get_data().decode())["error"], en_errors[error_code],
                         en_errors[error_code])

    def test_b_without_users_list(self):
        response = self.tst_zone()
        self.asset_master(response, 70)
        data["user"] = [1, 2, 3]

    def test_c_without_label(self):
        response = self.tst_zone()
        self.asset_master(response, 111)
        data["label"] = 1

    def test_d_with_incorrect_label(self):
        response = self.tst_zone()
        self.asset_master(response, 110)
        data["label"] = "penguin"
