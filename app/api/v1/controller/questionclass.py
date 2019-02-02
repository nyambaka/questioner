from .abs_controller import AbsController
from .display import Display


class Question(AbsController):

    def __init__(self, data):
        self.data = data

    def modify_for_insert(self):
        pass

    def modify_for_display(self):
        copy = self.data.copy()
        question_feedback = copy
        del question_feedback["vote"]
        del question_feedback["down"]
        del question_feedback["comment"]
        self._display.data = self.data
        return self

    def is_set(self, key):
        return key in self.data.keys()

    def type_check(self, key, type_claim):
        return isinstance(self.data[key], type_claim)

    def get_data(self):
        return self.data

    def get_display_data(self):
        return self._display.data

    def input_validate(self):
        if not isinstance(self.data, dict):
            return self.premature_return(214)
        if not self.is_set("userid"):
            return self.premature_return(201)
        if not self.type_check("userid", int):
            return self.premature_return(202)
        if not self.is_set("body"):
            return self.premature_return(205)
        if not self.type_check("body", str):
            return self.premature_return(206)
        if not self.is_set("meetup"):
            return self.premature_return(217)
        if not self.type_check("meetup", int):
            return self.premature_return(218)
        return self

    def second_validate(self):
        if not self.is_set("comment"):
            return self.premature_return(211)
        if not self.type_check("comment", list):
            return self.premature_return(212)
        if not self.is_set("vote"):
            return self.premature_return(207)
        if not self.type_check("vote", int):
            return self.premature_return(208)
        if not self.is_set("down"):
            return self.premature_return(209)
        if not self.type_check("down", int):
            return self.premature_return(210)
        if not self.is_set("id"):
            return self.premature_return(203)
        if not self.type_check("id", int):
            return self.premature_return(204)
        return self

    def modify_for_save(self, id_dictionary):
        self.data["vote"] = 0
        self.data["down"] = 0
        self.data["comment"] = []
        self.data["id"] = self.id_generator(id_dictionary, "question")
        self._display.data = self.data
        return self

    def save(self):
        if not self.is_set("meetup"):
            return self.premature_return(217)
        for i in self.save_to:
            if i["id"] == self.data["meetup"]:
                i["question"].append(self.get_data())
                return self
        self._display.data_error = 69
        return self

    def save_to(self, container):
        self.save_to = container
        return self

    def error_check(self):
        try:
            n = self._display.data_error
            return Display().error_display(self._display.data_error, 400)
        except:
            pass
