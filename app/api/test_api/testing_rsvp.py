import unittest
from app.api.v1 import application
import json

data = ""
sample_meeup = {
    "label": "meetup",
    "user": [1, 2]
}


class TestRsvp(unittest.TestCase):

    def setUp(self):
        self.app = application.test_client()
        self.url_prefix = ""

    def test_a_setting_up_a_meeting(self):
        global sample_meeup
        response = self.app.post(self.url_prefix + "/meetups", data=json.dumps(sample_meeup),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200, "posting a user should be possible")
        self.assertEqual(json.loads(response.get_data().decode())["id"], 1, "response should be correct")

    def test_b_post_empty(self):
        global data
        response = self.app.post(self.url_prefix + "/meetups/1/rsvp", data=json.dumps(data),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code,200,"correct response code")
        self.assertEqual(json.loads(response.get_data().decode()),"rsvp data should be of type json","correct response")
        data={}

    def test_c_test_with(self):
        response= self.tst_zone()
        self.assertEqual(json.loads(response.get_data().decode()), "provide a user id",
                         "correct response")
        data["userid"]="dfj"

    def tst_zone(self):
        response = self.app.post(self.url_prefix + "/meetups/1/rsvp", data=json.dumps(data),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200, "correct response code")
        return response

    def test_d_with_incorrect_user_id(self):
        response= self.tst_zone()
        self.assertEqual(json.loads(response.get_data().decode()), "user id should be of type integer",
                         "correct response")
        data["userid"] = 1

    def test_e_withiout(self):
        response= self.tst_zone()
        self.assertEqual(json.loads(response.get_data().decode()), "rsvp has not been set",
                         "correct response")
        data["rsvp"] = "nothing"

    def test_f_with_incorrect_rsvp(self):
        response= self.tst_zone()
        self.assertEqual(json.loads(response.get_data().decode()), "rsvp should be a yes no or maybe",
                         "correct response")
        data["rsvp"] = "yes"

    def test_g_test_withoud(self):
        response= self.tst_zone()
        self.assertEqual(json.loads(response.get_data().decode()), "meetup has not been set",
                         "correct response")
        data["meetup"] =1

    def test_h_test_with_incorrect_meetup(self):
        response= self.tst_zone()
        self.assertEqual(json.loads(response.get_data().decode())["message"], "successfully updated your rsvp",
                         "correct response")