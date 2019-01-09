class Comment:
    def __init__(self, data):
        super(Comment, self).__init__()
        self.data = data

    def is_set(self, key=""):
        return key in self.data.keys()

    def type_check(self, key, type_claim):
        return isinstance(self.data[key], type_claim)

    def get_user_id(self):
        if not self.is_set("userid"):
            return 301
        return self.data["userid"]

    def set_user_id(self, new_user_id):
        if not isinstance(new_user_id, int):
            return 302
        self.data["userid"] = new_user_id
        return self

    def get_comment(self):
        if not self.is_set("Comment"):
            return 303
        return self.data["Comment"]

    def set_comment(self, new_comment):
        if not isinstance(new_comment, str):
            return 304
        self.data["Comment"] = new_comment

    def get_data(self):
        return self.data

    def self_validate(self):
        if not isinstance(self.data, dict):
            return 305
        if not self.is_set("userid"):
            return 301
        if not self.type_check("userid", int):
            return 302
        if not self.is_set("Comment"):
            return 303
        if not self.type_check("Comment", str):
            return 304
        return 0

# sample_comment={
# 	"userid":1,
# 	"Comment":"i think we should prioritize this one"
# }


# test=Comment(sample_comment)
# result=test.getData()
# print(result)
