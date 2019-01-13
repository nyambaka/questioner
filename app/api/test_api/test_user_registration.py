import  unittest
from app.api.v1 import  application
import json

class Test_user_registration(unittest.TestCase):

    def setUp(self):
        self.data= {
            "username":"nelson"
        }