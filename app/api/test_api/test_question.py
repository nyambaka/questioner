import  unittest
from app.api.v1 import  app
import json

class TestQuestion(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.url_prefix = ""
        self.sample_data ={
            "userid":1,
            "body":"how can i do it better",
            "meetup":1
        }
        self.meet_state = []

    def test_post_question(self):
        response = self.client.post(self.url_prefix+"/question",headers ={"Content-Type":"application/json"},data = json.dumps(self.sample_data))
        self.assertEqual(response.status_code,200,"posting in the meetup should be allowed")
        self.assertEqual(json.loads(response.get_data().decode("utf-8")), {'body': 'how can i do it better', 'userid': 1, 'id': 1, 'meetup': 1}  , "correct response should be given back")
        self.meet_state = json.loads(response.get_data().decode("utf-8"))

    def test_fetch_specific_question(self):
        response = self.client.patch(self.url_prefix + "/question/1", headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200, "upvoting should be allowed")
        self.assertNotEqual(json.loads(response.get_data().decode('utf-8')), [],
                            "initial meetup state should be and empty list")




if __name__ == "__main__":
    unittest.main()
