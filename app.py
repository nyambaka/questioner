from flask import Flask ,request ,jsonify

from app.api.v1.controller.meetupclass import MeetUp
from app.api.v1.controller.questionclass import Question
from app.api.v1.model.database import *
from app.api.v1.utils.utility import meet_up_add_breath, question_add_breath ,reflect_meetup ,reflect_question


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/meetups", methods=["get"])
def meetup():
    responses = []
    for i in meet_ups:
        responses.append(reflect_meetup(i))
    return jsonify(responses)



@app.route("/meetups", methods=["post"])
def post_meet_up():
    final = meet_up_add_breath(request.get_json(), ids)
    test = MeetUp(final)
    error = test.self_validate()
    if not error:
        print(final)
        meet_ups.append(final)
    return jsonify(reflect_meetup(final))




@app.route("/question" ,methods=["post"])
def post_question():
    buffer_value = question_add_breath(request.get_json())
    buffer_class = Question(buffer_value)
    error = buffer_class.self_validate()
    for i in meet_ups:
        if i["id"] == buffer_value["meetup"]:
            i["question"].append(buffer_class)
            return jsonify(reflect_question(buffer_class))
    return jsonify({
        "error":"the massage id does not correspond to existing database record"
    })


if __name__ == '__main__':
    app.run()
