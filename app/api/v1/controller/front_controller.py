class FrontController:

    def __init__(self, controller, data):
        self._controller = controller(data)

    def post(self, ids, storage):
        self._controller.new_display()
        self._controller.input_validate()
        self._controller.modify_for_save(ids)
        self._controller.save_to(storage)
        self._controller.save()
        self._controller.modify_for_display()
        response = self._controller.display()
        return response.render_internal_error()

    def get(self):
        pass
