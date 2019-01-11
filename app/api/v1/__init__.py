from flask import Flask, request, jsonify
from app.api.v1.controller.meetupclass import MeetUp
from app.api.v1.controller.questionclass import Question
from app.api.v1.model.database import *
from app.api.v1.controller.rsvpclass import Rsvp
from app.api.v1.utils.utility import meet_up_add_breath, question_add_breath, reflect_meetup, reflect_question, \
    id_generator, reflect_vote
from app.api.v1.controller.commentclass import Comment
from app.api.v1.utils.error_file import en_errors

app = Flask(__name__)


@app.route('/', methods=["get"])
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
        meet_ups.append(final)
        return jsonify(reflect_meetup(final))
    return jsonify({
        "error": en_errors[error]
    })


@app.route("/meetups/<meet_up_id>", methods=["get"])
def meet_up_specific(meet_up_id):
    for i in meet_ups:
        buffer = MeetUp(i)
        if buffer.get_meet_up_id() == int(meet_up_id):
            return jsonify(reflect_meetup(i))
    return jsonify({
        "error": "there is not meetup with that specic id"
    })


@app.route("/question", methods=["post"])
def post_question():
    buffer_value = question_add_breath(request.get_json(), ids)
    buffer_class = Question(buffer_value)
    error = buffer_class.self_validate()
    for i in meet_ups:
        if i["id"] == buffer_value["meetup"]:
            i["question"].append(buffer_class.get_data())
            return jsonify(
                reflect_question(buffer_value)
            )
    if int(error) != 0:
        return jsonify({
            "status": 622,
            "error": en_errors[error]
        })
    return jsonify({
        "error": en_errors[601]
    })


@app.route("/question/<question_id>/upvote", methods=["patch"])
def upvote(question_id):
    for m in meet_ups:
        for q in m["question"]:
            if q["id"] == int(question_id):
                q["vote"] = q["vote"] + 1
                return jsonify({"status": 200, "data": reflect_vote(m, m["question"].index(q))})
    return jsonify({
        "error ": "no question found with that id"
    })


@app.route("/question/<question_id>/downvote", methods=["patch"])
def down_vote(question_id):
    for m in meet_ups:
        for q in m["question"]:
            if q["id"] == int(question_id):
                q["vote"] = q["vote"] - 1
                return jsonify({"status": 200, "data": reflect_vote(m, m["question"].index(q))})
    return jsonify({
        "error ": "no question found with that id"
    })


@app.route("/meetups/<meetup_id>/rsvp", methods=["post"])
def post_rsvp(meetup_id):
    temp_rsvp = Rsvp(request.get_json())
    error = temp_rsvp.self_validate()
    if not error:
        for m in meet_ups:
            if m["id"] == int(meetup_id):
                m["rsvp"][request.get_json()["userid"]] = request.get_json()["rsvp"]
        return jsonify({
            "status": 201,
            "message": en_errors["cor-rsvp"]
        }
        )
    return jsonify(error)


@app.route("/look")
def remember():
    print(meet_ups)
    return "done"
