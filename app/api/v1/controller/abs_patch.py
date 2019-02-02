from .get_question import GetQuestion
class Patch():

    def __init__(self,data):
        self._controller=GetQuestion(data)
        self._controller.new_display()
        self.data=data

    def up_vote(self,id):
        int_id = int(id)
        self._controller.get(int_id)
        for i in self.data:
            if i["id"] == 1:
                for q in i["question"]:
                    q["vote"] += 1
        return self

    def down_vote(self,id):
        int_id = int(id)
        self._controller.get(int_id)
        for i in self.data:
            if i["id"] == 1:
                for q in i["question"]:
                    q["vote"] -= 1
        return self

    def show(self):
        result = self._controller.display()
        return result.render_internal_error()
