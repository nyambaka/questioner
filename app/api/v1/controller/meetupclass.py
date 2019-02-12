import datetime
from .abs_controller import AbsController


class MeetUp(AbsController):

    def __init__(self, data):
        self.data = data

    def premature_return(self, error_code):
        self._display.data_error = error_code
        return self

    def input_validate(self):
        if not isinstance(self.data, dict):
            return self.premature_return(112)
        if not self.is_set("user"):
            return self.premature_return(103)
        if not self.type_check("user", list):
            return self.premature_return(104)
        if not self.is_set("topic"):
            return self.premature_return(111)
        if not self.type_check("topic", str):
            return self.premature_return(110)
        if not self.is_set("on"):
            return self.premature_return(116)
        if not self.type_check("on", str):
            return self.premature_return(117)
        if not self.is_set("location"):
            return self.premature_return(80)
        if not self.type_check("location", str):
            return self.premature_return(81)
        try:
            datetime.datetime.strptime(self.data["on"], '%b %d %Y')
        except:
            return self.premature_return(118)
            return self
        return self

    def second_validation(self):
        if not self.is_set("id"):
            return self.premature_return(101)
        if not self.type_check("id", int):
            return self.premature_return(102)
        if not self.is_set("question"):
            return self.premature_return(106)
        if not self.type_check("question", list):
            return self.premature_return(107)
        if not self.is_set("rsvp"):
            return self.premature_return(113)
        if not self.type_check("rsvp", dict):
            return self.premature_return(114)
        return self

    def get_data(self):
        return self.data

    def modify_for_display(self):
        if not isinstance(self.data, dict):
            return self.premature_return(214)
        copy = self.data.copy()
        if not isinstance(self.data, dict):
            return self.premature_return(501)
        meetup_feedback = copy
        del meetup_feedback["question"]
        del meetup_feedback["rsvp"]
        if not self.is_set("user"):
            return self.premature_return(104)
        del meetup_feedback["user"]
        self._display.data = meetup_feedback
        return self

    def modify_for_insert(self):
        del self.data["id"]
        del self.data["question"]
        return self

    def type_check(self, key, value, ):
        return isinstance(self.data[key], value)

    def is_set(self, key):
        return key in self.data.keys()

    def save_to(self, containter):
        self.save_to = containter
        return self

    def save(self):
        self.save_to.append(self.data)
        return self

    def modify_for_save(self,ids):
        if not isinstance(self.data, dict):
            return self.premature_return(502)
        self.data["id"] = self.id_generator(ids, "meetup")
        self.data["question"] = []
        self.data["rsvp"] = {}
        if not "user" in self.data.keys():
            return self.premature_return(31131)
        if not self.type_check("user", list):
            return self.premature_return(104)
        for i in self.data["user"]:
            self.data["rsvp"][i] = "null"
        self._display.data = self.data
        return self

    def get_display_data(self):
        return self._display.data
