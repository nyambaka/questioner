import unittest
from app import create_app
import json

application = create_app()


class TestMeetups(unittest.TestCase):

    def setUp(self):
        self.client = application.test_client()
        self.url_prefix = "api/v1"
        self.data = {
            "user": [1, 2, 3],
            "topic": "cheetah",
            "on": "Jun 1 2045",
            "location":"sports club"
        }
        self.sample_question = {
            "userid": 1,
            "body": "how can this be done",
            "meetup": 1
        }
        self.sample_rsvp = {
            "userid": 1,
            "rsvp": "yes",
            "meetup": 1
        }

    def test_a_post_meetup(self):
        response = self.client.post(self.url_prefix + "/meetups", headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.data))
        result = json.loads(response.get_data().decode())
        self.assertEqual(result["data"]["id"], 1, "id should be one")
        self.assertEqual(result["data"]["topic"], "cheetah", "the topic should be correct")
        self.assertEqual(result["data"]["on"], "Jun 1 2045", "date should be correct")
        self.assertEqual(response.status_code, 201, "correct status code should be done")

    def test_b_get_specific_meetup(self):
        response = self.client.get(self.url_prefix + "/meetups/1", headers={"Content-Type": "application/json"},
                                   data=json.dumps(self.data))
        result = json.loads(response.get_data().decode())
        self.assertEqual(result["data"]["id"], 1, "id should be one")
        self.assertEqual(result["data"]["topic"], "cheetah", "the topic should be correct")
        self.assertEqual(result["data"]["on"], "Jun 1 2045", "date should be correct")
        self.assertEqual(result["data"]["user"], [1, 2, 3], "the users list should be correct")
        self.assertEqual(response.status_code, 201, "correct status code should be done")

    def test_c_posting_a_question(self):
        response = self.client.post(self.url_prefix + "/question", headers={"Content-Type": "application/json"},
                                    data=json.dumps(self.sample_question))
        result = json.loads(response.get_data().decode())
        self.assertEqual(response.status_code, 201, "correct status code should be returned")
        self.assertEqual(result["data"]["id"], 1, "id should be correct")
        self.assertEqual(result["data"]["body"], "how can this be done", "correct question should be brought back")
        self.assertEqual(result["data"]["meetup"], 1, "correct meetup should be reflected")
        self.assertEqual(result["data"]["userid"], 1, "correct userid should be returned")
        self.assertEqual(result["status"], 201, "correct status code should be reflected")

    def test_d_upvote(self):
        response = self.client.patch(self.url_prefix + "/question/1/upvote",
                                     headers={"Content-Type": "application/json"})
        result = json.loads(response.get_data().decode())
        self.assertEqual(response.status_code, 201, "correct id should be returned")
        self.assertEqual(result["status"], 201, "correct status code should be returned")
        self.assertEqual(result["data"][0]["id"], 1, "correct id should be returned")
        self.assertEqual(result["data"][0]["vote"], 1, "the correct topic for the meetup should be returned")

    def test_e_downvote(self):
        response = self.client.patch(self.url_prefix + "/question/1/downvote",
                                     headers={"Content-Type": "application/json"})
        result = json.loads(response.get_data().decode())
        self.assertEqual(response.status_code, 201, "correct id should be returned")
        self.assertEqual(result["status"], 201, "correct status code should be returned")
        self.assertEqual(result["data"][0]["id"], 1, "correct id should be returned")
        self.assertEqual(result["data"][0]["vote"], 0, "the correct topic for the meetup should be returned")

    def test_f_posting_rsvp(self):
        response = self.client.post(self.url_prefix + "/meetups/2/rsvp", data=json.dumps(self.sample_rsvp),
                                    headers={"Content-Type": "application/json"})
        result = json.loads(response.get_data().decode())
        self.assertEqual(response.status_code, 201, "correct status code should be returned")
        self.assertEqual(result["data"]["rsvp"], "yes", "correct response should be given back")
        self.assertEqual(result["status"], 201, "correct error message should be given back")
