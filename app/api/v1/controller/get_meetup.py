from .abs_get import AbstractGet

class GetMeetup(AbstractGet):

    def __init__(self,data):
        self.data = data


    def get_all(self):
        self._display.data = self.data
        return self

    def get_with_id(self, id):
        try:
            int(id)
        except:
            self._display.data_error = 204
            return self
        result = []
        for i in self.data:
            if i["id"] == int(id):
                self._display.data=i
                result.append(i)
        if result ==[]:
            self._display.data_error =220
        return self

