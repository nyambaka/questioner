class Question:
    """docstring for Question"""

    def __init__(self, data):
        self.data = data

    def is_set(self, key):
        return key in self.data.keys()

    def type_check(self, key, type_claim):
        return isinstance(self.data[key], type_claim)

    def get_user_id(self):
        if not self.is_set("userid"):
            return 201
        return self.data['userid']

    def set_user_id(self, new_id):
        if not isinstance(new_id, int):
            return 202
        self.data['userid'] = new_id
        return self

    def get_id(self):
        if not self.is_set("id"):
            return 203
        return self.data['id']

    def set_id(self, new_id):
        if not isinstance(new_id, int):
            return 204
        self.data['id'] = new_id

    def get_body(self):
        if not self.is_set("body"):
            return 205
        return self.data['body']

    def set_body(self, new_body):
        if not isinstance(new_body, str):
            return 206
        self.data['body'] = new_body
        return self

    def get_vote(self):
        if not self.is_set("vote"):
            return 207
        return self.data['vote']

    def set_vote(self, new_setvote):
        if not isinstance(new_setvote, int):
            return 208
        self.data['vote'] = new_setvote
        return self

    def add_vote(self):
        if not self.is_set("vote"):
            self.data["vote"] = 1
        else:
            self.data['vote'] = self.data['vote'] + 1

    def get_down(self):
        if not self.is_set("down"):
            return 209
        return self.data['down']

    def set_down(self, new_down):
        if not isinstance(new_down, int):
            return 210
        self.data['down'] = new_down
        return self

    def add_down(self):
        if not self.is_set("down"):
            self.data['down'] = 1
        else:
            self.data['down'] = self.data['down'] + 1
            return self

    def get_comment(self):
        if not self.is_set("comment"):
            return 211
        return self.data['comment']

    def set_comment(self, new_comment_list):
        if not isinstance(new_comment_list, list):
            return 212
        self.data['comment'] = new_comment_list
        return self

    def add_comment(self, new_comment):
        if not isinstance(new_comment, dict):
            return 213
        self.data['comment'].append(new_comment)
        return self

    def get_meetup(self):
        if not self.is_set("meetup"):
            return 217
        return self.data['meetup']

    def set_meetup(self, meetup):
        if not isinstance(meetup, int):
            return 218
        self.data['meetup'] = meetup
        return self

    def get_data(self):
        return self.data

    def self_validate(self):
        if not isinstance(self.data, dict):
            return 214
        if not self.is_set("userid"):
            return 201
        if not self.type_check("userid", int):
            return 202
        if not self.is_set("id"):
            return 203
        if not self.type_check("id", int):
            return 204
        if not self.is_set("body"):
            return 205
        if not self.type_check("body", str):
            return 206
        if not self.is_set("vote"):
            return 207
        if not self.type_check("vote", int):
            return 208
        if not self.is_set("down"):
            return 209
        if not self.type_check("down", int):
            return 210
        if not self.is_set("comment"):
            return 211
        if not self.type_check("comment", list):
            return 212
        if not self.is_set("meetup"):
            return 217
        if not self.type_check("meetup", int):
            return 218
        return 0

# samplequestion={
# 	"userid":1,
# 	"id":2,
# 	"vote":34,
# 	"down":78,
# 	"comment":[],
# 	"body":"is python healthy to consume"

# }

# test=Question(samplequestion)
# result= test.selfValidate()
# print(result)
