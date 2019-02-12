from .abs_get import AbstractGet


class GetQuestion(AbstractGet):

    def __init__(self, data):
        self.data = data

    def get(self, id=-1):
        self.new_display()
        if id == -1:
            self.get_all()
            return self
        self.get_with_id(id)

    def get_with_id(self, id):
        try:
            int(id)
        except:
            self._display.data_error = 204
            return self
        result = []
        for i in self.data:
            for q in i["question"]:
                if q['id'] == int(id):
                    self._display.data = q
                    result = self.data[self.data.index(i)]["question"]
        if result == []:
            self._display.data_error = 220
            return self
        self._display.data = result
        return self

    def get_all(self):
        result = []
        for i in self.data:
            if i["id"] == 1:
                result += self.data[self.data.index(i)]["question"]
        self._display.data = result
        return self
