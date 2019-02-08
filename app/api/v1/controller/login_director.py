class LoginDirector:

    def __init__(self,controller,data,database):
        self._controller = controller(data,database)
        self._controller.new_display()


    def login_user(self):
        self._controller.input_validate()
        try:
            self._controller._display.data_error
        except:
            if self._controller.is_set("username"):
                return self._controller.login_with_username()
            if self._controller.is_set("email"):
                return self._controller.login_with_email()
        return self


    def display(self):
        response = self._controller.get_display()
        return response.render_internal_error()

    def login(self):
        self.login_user()
        return self.display()