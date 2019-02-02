from  app.api.v1.controller.abs_controller import AbsController

class Rsvp(AbsController):
    def __init__(self, data):
        self.data = data

    def is_set(self, key):
        return key in self.data.keys()

    def type_check(self, key, claim_type):
        print(self.data)
        return isinstance(self.data[key], claim_type)


    def input_validate(self):
        if not isinstance(self.data, dict):
            return self.premature_return( 57)
        if not self.is_set("userid"):
            return self.premature_return(51)
        if not self.type_check("userid", int):
            return self.premature_return(52)
        if not self.is_set("rsvp"):
            return self.premature_return(54)
        if not self.type_check("rsvp", str):
            return self.premature_return(53)
        if not self.data["rsvp"].lower() in ["yes", "no", "maybe"]:
            return self.premature_return(58)
        if not self.is_set("meetup"):
            return self.premature_return(55)
        if not self.type_check("meetup", int):
            return self.premature_return(56)
        return self

    def save_to(self, containter):
        self.save_to = containter
        return self

    def save(self):
        for m in self.save_to:
            if self.data["meetup"] == m["id"]:
                m["rsvp"][self.data["userid"]]= self.data["rsvp"]
        return self

    def modify_for_insert(self):
        return self

    def modify_for_save(self,ids):
        return self

    def modify_for_display(self):
        self._display.data = self.data
        return self

    def get_data(self):
        return self
