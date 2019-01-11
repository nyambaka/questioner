class Rsvp:
    def __init__(self, data):
        self.data = data

    def is_set(self, key):
        return key in self.data.keys()

    def type_check(self, key, claim_type):
        print(self.data)
        return isinstance(self.data[key], claim_type)

    def get_user_id(self):
        if not self.is_set("userid"):
            return 801
        return self.data["userid"]

    def set_user_id(self, new_id):
        if not isinstance(new_id, int):
            return 804
        self.data["userid"] = new_id

    def set_rsvp(self, new_rsvp):
        if not isinstance(new_rsvp, str):
            return 802
        self.data["userid"] = new_rsvp
        return self

    def get_rsvp(self):
        if not self.is_set("rsvp"):
            return 803
        return self.data["rsvp"]

    def get_meetup(self):
        if not self.is_set("meetup"):
            return 806
        return self.data["meetup"]

    def set_meetup(self, new_meetup):
        if not isinstance(new_meetup, int):
            return 807
        self.data["meetup"] = new_meetup

    def self_validate(self):
        if not isinstance(self.data, dict):
            return 808
        if not self.is_set("userid"):
            return 801
        if not self.type_check("userid", int):
            return 804
        if not self.is_set("rsvp"):
            return 803
        if not self.type_check("rsvp", str):
            return 802
        if not self.data["rsvp"].lower() in ["yes", "no", "maybe"]:
            return 805
        if not self.is_set("meetup"):
            return 806
        if not self.type_check("meetup", int):
            return 807
        return 0
