import unittest
from app import create_app
from app.api.v1.utils.error_file import en_errors
import json

application = create_app()


class TestMeetups(unittest.TestCase):

    def setUp(self):
        self.client = application.test_client()
        self.url_prefix = "api/v1"
        self.data = {
            "user": [1, 2, 3],
            "label": "cheetah",
            "on": "Jun 1 2005"
        }
        self.sample_question = {
            "userid": 1,
            "body": "how can this be done",
            "meetup": 2
        }
        self.sample_rsvp = {
            "userid": 1,
            "rsvp": "yes",
            "meetup": 2
        }

    def test_a_post_meetup(self):
        response = self.client.post(self.url_prefix + "/meetups", headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.data))
        result = json.loads(response.get_data().decode())
        self.assertEqual(result["data"]["id"], 2, "id should be one")
        self.assertEqual(result["data"]["label"], "cheetah", "the label should be correct")
        self.assertEqual(result["data"]["on"], "Jun 1 2005", "date should be correct")
        self.assertEqual(result["data"]["user"], [1, 2, 3], "the users list should be correct")
        self.assertEqual(response.status_code, 201, "correct status code should be done")

    def test_b_get_specific_meetup(self):
        response = self.client.get(self.url_prefix + "/meetups/2", headers={"Content-Type": "application/json"},
                                   data=json.dumps(self.data))
        result = json.loads(response.get_data().decode())
        self.assertEqual(result["data"]["id"], 2, "id should be one")
        self.assertEqual(result["data"]["label"], "cheetah", "the label should be correct")
        self.assertEqual(result["data"]["on"], "Jun 1 2005", "date should be correct")
        self.assertEqual(result["data"]["user"], [1, 2, 3], "the users list should be correct")
        self.assertEqual(response.status_code, 201, "correct status code should be done")

    def test_c_posting_a_question(self):
        response = self.client.post(self.url_prefix + "/question", headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.sample_question))
        result = json.loads(response.get_data().decode())
        self.assertEqual(response.status_code, 201, "correctt status code should be returned")
        self.assertEqual(result["data"]["id"], 1, "id should be correct")
        self.assertEqual(result["data"]["body"], "how can this be done", "correct question should be brought back")
        self.assertEqual(result["data"]["meetup"], 2, "correct meetup should be reflected")
        self.assertEqual(result["data"]["userid"], 1, "correct userid should be returned")
        self.assertEqual(result["status"], 201, "correct status code should be reflected")

    def test_d_upvote(self):
        response = self.client.patch(self.url_prefix + "/question/1/upvote",
                                     headers={"Content-Type": "application/json"})
        result = json.loads(response.get_data().decode())
        self.assertEqual(response.status_code, 200, "correct id should be returned")
        self.assertEqual(result["status"], 200, "correct status code should be returned")
        self.assertEqual(result["data"]["id"], 2, "correct id should be returned")
        self.assertEqual(result["data"]["label"], "cheetah", "the correct label for the meetup should be returned")
        self.assertEqual(result["data"]["vote"], 1, "the correct label for the meetup should be returned")
        self.assertEqual(result["data"]["on"], "Jun 1 2005", "correct date should be returned")

    def test_e_downvote(self):
        response = self.client.patch(self.url_prefix + "/question/1/downvote",
                                     headers={"Content-Type": "application/json"})
        result = json.loads(response.get_data().decode())
        self.assertEqual(response.status_code, 200, "correct id should be returned")
        self.assertEqual(result["status"], 200, "correct status code should be returned")
        self.assertEqual(result["data"]["id"], 2, "correct id should be returned")
        self.assertEqual(result["data"]["label"], "cheetah", "the correct label for the meetup should be returned")
        self.assertEqual(result["data"]["vote"], 0, "the correct label for the meetup should be returned")
        self.assertEqual(result["data"]["on"], "Jun 1 2005", "correct date should be returned")

    def test_f_posting_rsvp(self):
        response = self.client.post(self.url_prefix + "/meetups/2/rsvp", data=json.dumps(self.sample_rsvp),
                                    headers={"Content-Type": "application/json"})
        result = json.loads(response.get_data().decode())
        self.assertEqual(response.status_code, 201, "correct status code should be returned")
        self.assertEqual(result["message"], "successfully updated your rsvp", "correct response should be given back")
        self.assertEqual(result["status"], 201, "correct error message should be given back")
