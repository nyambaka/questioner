from flask import Flask

from app.api.v1.controller.meetupclass import MeetUp
from app.api.v1.controller.questionclass import Question
from app.api.v1.model.database import *
from app.api.v1.utils.utility import meet_up_add_breath, question_add_breath ,reflect_meetup


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/meetup", methods=["get"])
def meetup():
    value = []
    for i in meet_ups:
        value.append(reflect_meetup(i))
    return value



if __name__ == '__main__':
    app.run()
