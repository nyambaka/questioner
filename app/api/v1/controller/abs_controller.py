import abc
from app.api.v1.controller.display import Display

class AbsController(metaclass=abc.ABCMeta):

    def __init__(self,data):
        self.data=data

    def new_display(self):
        self._display=Display()

    def premature_return(self,error_code):
        self._display.data_error = error_code
        return self

    def display(self):
        return self._display

    @abc.abstractmethod
    def input_validate(self):
        pass

    @abc.abstractmethod
    def modify_for_display(self):
        pass

    @abc.abstractmethod
    def modify_for_insert(self):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass


    def id_generator(self,ids, key):
        if key in ids.keys():
            ids[key] = ids[key] + 1
            return ids[key]
        ids[key] = 1
        return ids[key]

    @abc.abstractmethod
    def save_to(self,to):
        pass

    @abc.abstractmethod
    def save(self):
        pass

    @abc.abstractmethod
    def modify_for_save(self):
        pass