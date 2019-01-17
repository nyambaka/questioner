import datetime


class MeetUp:
    def __init__(self, data):
        self.data = data

    def type_check(self, key, value, ):
        return isinstance(self.data[key], value)

    def is_set(self, key):
        return key in self.data.keys()

    def get_meet_up_id(self):
        if not self.is_set("id"):
            return 101
        else:
            return self.data['id']

    def set_meet_up_id(self, new_id):
        if not isinstance(new_id, int):
            return 102
        else:
            self.data["id"] = new_id
            return self

    def set_meet_up_topic(self, new_topic):
        if not self.type_check(new_topic, str):
            return 110
        self.data['topic'] = new_topic
        return self

    def get_meet_up_topic(self):
        if not self.is_set("topic"):
            return 111
        return self.data['topic']

    def get_user(self):
        if not self.is_set("user"):
            return 103
        else:
            return self.data['user']

    def set_user(self, new_user):
        if not isinstance(new_user, list):
            return 104
        else:
            self.data['user'] = new_user
            return self

    def add_single_user(self, new_id):
        if not isinstance(new_id, int):
            return 105
        if not self.is_set('user'):
            self.data['user'] = [new_id]
        else:
            self.data['user'].append(new_id)
            return self

    def get_question(self):
        if not self.is_set("question"):
            return 106
        else:
            return self.data['question']

    def add_question(self, new_question):
        if not isinstance(new_question, dict):
            return 107
        else:
            self.data['question'].append(new_question)
            return self

    def get_number_of_question(self):
        if not self.is_set("question"):
            return 108
        else:
            return len(self.data['question'])

    def get_number_of_user(self):
        if not self.is_set("user"):
            return 109
        else:
            return len(self.data['user'])

    def get_data(self):
        return self.data

    def get_rsvp(self):
        if not self.is_set("rsvp"):
            return 113
        return self.data["rsvp"]

    def get_date(self):
        if not self.is_set("on"):
            return 80
        return self.data["on"]

    def set_date(self,new_date):
        if not self.type_check("on"):
            return 82
        self.data["on"] = new_date

    def set_rsvp(self, new_rsvp):
        if not isinstance(new_rsvp, dict):
            return 114
        self.data["rsvp"] = new_rsvp
        return self

    def self_validate(self):
        if not isinstance(self.data, dict):
            return 112
        if not self.is_set("id"):
            return 101
        if not self.type_check("id", int):
            return 102
        if not self.is_set("user"):
            return 103
        if not self.type_check("user", list):
            return 104
        if not self.is_set("question"):
            return 106
        if not self.type_check("question", list):
            return 107
        if not self.is_set("topic"):
            return 111
        if not self.type_check("topic", str):
            return 110
        if not self.is_set("rsvp"):
            return 113
        if not self.type_check("rsvp", dict):
            return 114
        if not self.is_set("on"):
            return 116
        if not self.type_check("on", str):
            return 117
        if not self.is_set("location"):
            return 80
        if not self.type_check("location", str):
            return 81
        try:
            datetime.datetime.strptime(self.data["on"], '%b %d %Y')
        except:
            return 118
        return 0

# samplemeetup={
# 	"id":1,
# 	"user":[],
# 	"question":[],
# 	"topic":"team"
# }
