import abc
from .display import Display


class AbstractGet(metaclass=abc.ABCMeta):

    def new_display(self):
        self._display=Display()

    def display(self):
        return self._display

    @abc.abstractmethod
    def get_with_id(self,id):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass
