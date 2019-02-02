class GetFrontController(object):
    def __init__(self, controller, data):
        self._controller = controller(data)

    def get(self, id=-1):
        self._controller.new_display()
        if id == -1:
            self._controller.get_all()
            return self
        self._controller.get_with_id(id)
        return self

    def show(self):
        result = self._controller.display()
        return result.render_internal_error()