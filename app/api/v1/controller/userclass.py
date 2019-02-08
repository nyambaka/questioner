from app.api.v1.controller.abs_controller import AbsController


class User(AbsController):

    def __init__(self, data):
        self.data = data

    def is_set(self, key):
        return key in self.data.keys()

    def type_check(self, key, suspected_type):
        return isinstance(self.data[key], suspected_type)

    def input_validate(self):
        if not isinstance(self.data, dict):
            return self.premature_return(419)
        if not self.is_set("firstname"):
            return self.premature_return(403)
        if not self.type_check("firstname", str):
            return self.premature_return(404)
        if not self.is_set("lastname"):
            return self.premature_return(405)
        if not self.type_check("lastname", str):
            return self.premature_return(406)
        if not self.is_set("othername"):
            return self.premature_return(407)
        if not self.type_check("othername", str):
            return self.premature_return(408)
        if not self.is_set("email"):
            return self.premature_return(409)
        if not self.type_check("email", str):
            return self.premature_return(410)
        if not self.is_set("phonenumber"):
            return self.premature_return(411)
        if not self.type_check("phonenumber", str):
            return self.premature_return(412)
        if not self.is_set("username"):
            return self.premature_return(413)
        if not self.type_check("username", str):
            return self.premature_return(414)
        if not self.is_set("registered"):
            return self.premature_return(415)
        if not self.type_check("registered", str):
            return self.premature_return(416)
        if not self.is_set("isadmin"):
            return self.premature_return(417)
        if not self.type_check("isadmin", int):
            return self.premature_return(418)
        if not self.is_set("password"):
            return self.premature_return(419)
        if not self.type_check("password", str):
            return self.premature_return(420)
        return self

    def save_to(self, containter):
        self.save_to = containter
        return self

    def save(self):
        self.save_to.append(self.data)
        return self

    def modify_for_save(self,ids):
        if not isinstance(self.data, dict):
            return self.premature_return(502)
        self.data["id"] = self.id_generator(ids, "user")
        return self

    def get_data(self):
        return self.data

    def modify_for_display(self):
        self._display.data = self.data
        return self

    def modify_for_insert(self, ids):
        if not isinstance(self.data, dict):
            return self.premature_return(502)
        self.data["id"] = self.id_generator(ids, "user")
        return self
