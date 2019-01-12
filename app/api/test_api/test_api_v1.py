import  unittest
from app.api.v1 import  application
import json

class TestMeetups(unittest.TestCase):

    def setUp(self):
        application.config['TESTING'] = True
        self.client = application.test_client()
        self.url_prefix = ""
        self.sample_data ={
            "label":"meetup eleven",
            "user":[1,3,4]
        }
        self.meet_state = []


    def test_post_meetup(self):
        response = self.client.post(self.url_prefix+"/meetups",headers ={"Content-Type":"application/json"},data = json.dumps(self.sample_data))
        self.assertEqual(response.status_code,200,"posting in the meetup should be allowed")
        self.assertEqual(json.loads(response.get_data().decode("utf-8")), {'user': [1, 3, 4], 'id': 1, 'label': 'meetup eleven'} , "correct response should be given back")

    def test_status_code(self):
        response = self.client.get(self.url_prefix + "/meetups",headers={"Content-Type":"application/json"})
        self.assertEqual(response.status_code,200 ,"meetup record should be empty initally")
        self.assertEqual(json.loads(response.get_data().decode('utf-8')), [{'user': [1, 3, 4], 'id': 1, 'label': 'meetup eleven'}] ,"initial meetup state should be and empty list")

    def test_fetch_specific_meetup(self):
        response = self.client.get(self.url_prefix + "/meetups/1", headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200, "fetching a meetup with correct id should be returned correctly")
        self.assertNotEqual(json.loads(response.get_data().decode('utf-8')), [],
                            "initial meetup state should be and empty list")

    def testing_none_existing_meetup(self):
        response = self.client.get(self.url_prefix + "/meetups/99", headers={"Content-Type": "application/json"})
        self.assertEqual(json.loads(response.get_data().decode('utf-8'))["error"],'there is not meetup with that specic id',
                            "initial meetup state should be and empty list")


