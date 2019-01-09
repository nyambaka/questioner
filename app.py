from flask import Flask ,request ,jsonify
from app.api.v1.controller.meetupclass import MeetUp
from app.api.v1.controller.questionclass import Question
from app.api.v1.model.database import *
from app.api.v1.utils.utility import meet_up_add_breath, question_add_breath ,reflect_meetup,reflect_question, id_generator
from app.api.v1.controller.commentclass import Comment


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


@app.route("/meetup/<meet_up_id>" )
def meet_up_specific(meet_up_id):
    for i in meet_ups:
        buffer = MeetUp(i)
        print(buffer.get_meet_up_id())
        if buffer.get_meet_up_id() == int(meet_up_id):
            return jsonify(reflect_meetup(i))
    return jsonify({
        "error":"there is not meetup with that specic id"
    })

@app.route("/question" ,methods=["post"])
def post_question():
    buffer_value = question_add_breath(request.get_json(),ids)
    buffer_class = Question(buffer_value)
    error = buffer_class.self_validate()
    print(error)
    for i in meet_ups:
        if i["id"] == buffer_value["meetup"]:
            i["question"].append(buffer_class.get_data())
            print(buffer_class.get_data())
            return jsonify({
                "message":"meetup found "
            })
    return jsonify({
        "error":"the massage id does not correspond to existing database record"
    })


@app.route("/question/<question_id>", methods=["patch"])
def upvote(question_id):
    for m in meet_ups:
        for q in m["question"]:
            if q["id"] == int(question_id):
                q["vote"] = q["vote"] +1
                return "done"
            return jsonify({
                "error ":"no question found with that id"
            })



@app.route("/look")
def remember():
    print(meet_ups)
    return "done"


if __name__ == '__main__':
    app.run()
