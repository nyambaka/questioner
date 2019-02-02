from app.api.v1.controller.display import Display


class Login:
    def __init__(self, data,database):
        self.data = data
        self._database = database
        self.logged_in=False

    def new_display(self):
        self._display = Display()

    def get_display(self):
        return self._display

    def type_check(self, key, type_claim):
        return isinstance(self.data[key], type_claim)

    def premature_return(self, error):
        self._display.data_error = error
        return self

    def input_validate(self):
        if not self.is_set("username"):
            if not self.is_set("email"):
                return self.premature_return(222)
        if not self.is_set("password"):
            return self.premature_return(419)
        if not self.type_check("password", str):
            return self.premature_return(420)
        return self



    def is_set(self, key):
        return key in self.data.keys()

    def login_with_username(self):
        for user in self._database:
            if self.data["username"] == user["username"] and self.data["password"] == user["password"]:
                self._display.data = user
                self.logged_in=True
        if self.logged_in == False:
            return self.premature_return(224)
        return self

    def login_with_email(self):
        for user in self._database:
            if self.data["email"] == user["email"] and self.data["password"] == user["password"]:
                self._display.data = user
                self.logged_in = True
        if self.logged_in == False:
            return self.premature_return(224)
        return self

