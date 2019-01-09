import  unittest
from app.api.v1 import  app


class TestMeetups(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_status_code(self):
        response = self.client.get("/meetups")
        self.assertEqual(response.status_code,200 ,"meetup record should be empty initally")