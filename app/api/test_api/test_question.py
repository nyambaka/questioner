import  unittest
from app import  create_app
import json
from app.api.v1.utils.error_file import en_errors
application =create_app()

class TestQuestion(unittest.TestCase):

    def setUp(self):
        self.client = application.test_client()
        self.url_prefix = "api/v1"
        self.sample_data ={
            "userid":1,
            "body":"how can i do it better",
            "meetup":1
        }
        self.meet_state = []

    def test_post_question(self):
        response = self.client.post(self.url_prefix+"/question",headers ={"Content-Type":"application/json"},data = json.dumps(self.sample_data))
        self.assertEqual(response.status_code,400,"posting in the meetup should be allowed")
        self.assertEqual(json.loads(response.get_data().decode())["error"], en_errors[601], "correct response should be given back")
        self.meet_state = json.loads(response.get_data().decode())

    def test_fetch_specific_question(self):
        response = self.client.patch(self.url_prefix + "/question/1/upvote", headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200, "upvoting should be allowed")
        self.assertNotEqual(json.loads(response.get_data().decode('utf-8')), {'body': 'how can i do it better', 'id': 1, 'meetup': 1, 'userid': 1},
                            "initial meetup state should be and empty list")



class TestUP(unittest.TestCase):
    def setUp(self):
        self.client = application.test_client()
        self.data = 1

    def test_upvote(self):
        resp = self.client.patch("/")


if __name__ == "__main__":
    unittest.main()
