from flask import Flask, request, jsonify, Blueprint
from app.api.v1.controller.meetupclass import MeetUp
from app.api.v1.controller.questionclass import Question
from app.api.v1.controller.userclass import User
from app.api.v1.model.database import *
from app.api.v1.controller.rsvpclass import Rsvp
from app.api.v1.utils.utility import meet_up_add_breath, question_add_breath, reflect_meetup, reflect_question, \
    id_generator, reflect_vote, user_add_breath, validate_user_login_details
from app.api.v1.utils.error_file import en_errors
from datetime import datetime

application = Flask(__name__)
blueprint = Blueprint('blueprint', __name__)


@blueprint.route("/meetups", methods=["get"])
def meetup():
    responses = []
    for i in meet_ups:
        responses.append(reflect_meetup(i))
    return jsonify(
        {
            "status": 200,
            "data": responses
        }
    ), 200


@blueprint.route("/meetups", methods=["post"])
def post_meet_up():
    if invalid_json():
        return invalid_json()
    final = meet_up_add_breath(request.get_json(), ids)
    if final == 31131:
        return jsonify(
            {
                "error": en_errors[70]
            }
        ), 400
    test = MeetUp(final)
    error = test.self_validate()
    if not error:
        if not datetime.strptime(test.get_date(), '%b %d %Y') > datetime.now():
            return jsonify({
                "error": en_errors[82],
                "status": 400
            }), 400
        meet_ups.append(final)
        return jsonify({
            "status": 201,
            "data": reflect_meetup(final)
        }
        ), 201
    print(error)
    return jsonify({
        "error": en_errors[error]
    }), 400


@blueprint.route("/meetups/<meet_up_id>", methods=["get"])
def meet_up_specific(meet_up_id):
    if invalid_id(meet_up_id):
        return invalid_id(meet_up_id)
    for i in meet_ups:
        buffer = MeetUp(i)
        if buffer.get_meet_up_id() == int(meet_up_id):
            return jsonify(
                {
                    "status": 201,
                    "data": reflect_meetup(i)
                }
            ), 201
    return jsonify({
        "status": 400,
        "error": en_errors[69]
    }), 400


@blueprint.route("/question", methods=["post"])
def post_question():
    if invalid_json():
        return invalid_json()
    buffer_value = question_add_breath(request.get_json(), ids)
    buffer_class = Question(buffer_value)
    error = buffer_class.self_validate()
    if error:
        return jsonify({
            "status": 400,
            "error": en_errors[error]
        }), 400
    for i in meet_ups:
        if i["id"] == buffer_value["meetup"]:
            i["question"].append(buffer_class.get_data())
            return jsonify(
                {
                    "status": 201,
                    "data": reflect_question(buffer_value)
                }
            ), 201

    if int(error) != 0:
        return jsonify({
            "status": 400,
            "error": en_errors[error]
        }), 400

    return jsonify({
        "error": en_errors[601]
    }), 400


@blueprint.route("/question/<question_id>/upvote", methods=["patch"])
def upvote(question_id):
    if invalid_id(question_id):
        return invalid_id(question_id)
    for m in meet_ups:
        for q in m["question"]:
            if q["id"] == int(question_id):
                q["vote"] = q["vote"] + 1
                return jsonify({"status": 200, "data": reflect_vote(m, m["question"].index(q))})
    return jsonify({
        "error ": en_errors[72]
    })


@blueprint.route("/question/<question_id>/downvote", methods=["patch"])
def down_vote(question_id):
    if invalid_id(question_id):
        return invalid_id(question_id)
    for m in meet_ups:
        for q in m["question"]:
            if q["id"] == int(question_id):
                q["vote"] = q["vote"] - 1
                return jsonify({"status": 200, "data": reflect_vote(m, m["question"].index(q))})
    return jsonify({
        "error ": en_errors[71]
    })


@blueprint.route("/meetups/<meetup_id>/rsvp", methods=["post"])
def post_rsvp(meetup_id):
    if invalid_json():
        return invalid_json()
    if invalid_id(meetup_id):
        return invalid_id(meetup_id)
    temp_rsvp = Rsvp(request.get_json())
    error = temp_rsvp.self_validate()
    if not error:
        for m in meet_ups:
            if m["id"] == int(meetup_id):
                if not request.get_json()["meetup"] == int(meetup_id):
                    return jsonify({
                        "status":400,
                        "error":en_errors[79]
                    }),400
                if not datetime.strptime(m["on"], '%b %d %Y') > datetime.now():
                    return jsonify({
                        "error":en_errors[78],
                        "status":400
                    }),400
                m["rsvp"][request.get_json()["userid"]] = request.get_json()["rsvp"]
                return jsonify({
                    "status": 201,
                    "data":{
                        "topic":m["topic"],
                        "meetup":m["id"],
                        "status":request.get_json()["rsvp"]
                    }
                }), 201
        return jsonify(
            {
                "status": 400,
                "error": en_errors[59]
            }
        ), 400
    return jsonify({
        "error":en_errors[error],
        "status":400
    })


@blueprint.route("/look")
def remember():
    return jsonify(
        {
            "status": 200,
            "data": meet_ups
        }
    )


@blueprint.route("/signup", methods=["post"])
def sign_up():
    if invalid_json():
        return invalid_json()
    data = user_add_breath(request.get_json(), ids)
    tempUser = User(data)
    error = tempUser.self_validate()
    if not error:
        for i in users:
            sample = User(i)
            if sample.get_user_name() == tempUser.get_user_name():
                return jsonify(
                    {
                        "error": en_errors[801]
                    }
                ), 400
            if sample.get_email() == tempUser.get_email():
                return jsonify(
                    {
                        "errror": en_errors[802]
                    }
                ), 400
        users.append(tempUser.get_data())
        return jsonify(
            {"status": 201,
             "data": tempUser.get_data()
             }
        ), 201
    return jsonify({
        "error": en_errors[error]
    }), 400


@blueprint.route("/login", methods=["post"])
def login():
    if invalid_json():
        return invalid_json()
    if validate_user_login_details(request.get_json()) == 0:
        for i in users:
            temp_user = User(i)
            data = request.get_json()
            if "email" in data.keys():
                if temp_user.get_email() == data["email"] and temp_user.get_password() == request.get_json()[
                    "password"]:
                    login_user.append(temp_user.get_id())
                    return jsonify({
                        "status": 201,
                        "data": en_errors[75]
                    }), 201
            if "username" in data.keys():
                if temp_user.get_user_name() == data["username"] and temp_user.get_password() == request.get_json()[
                    "password"]:
                    login_user.append(temp_user.get_id())
                    return jsonify({
                        "status": 201,
                        "data": en_errors[75]
                    }), 201
    if validate_user_login_details(request.get_json()) != 0:
        return jsonify({
            "error": en_errors[validate_user_login_details(request.get_json())]
        }), 400
    return jsonify({
        "error": en_errors[711]
    }), 400


@blueprint.route("/meetups/upcomings")
def upcoming_meetups():
    events = []
    for m in meet_ups:
        if datetime.strptime(m["on"], '%b %d %Y') > datetime.now():
            events.append(m)
    return jsonify({
        "data": events,
        "status": 200
    })


def invalid_id(variable):
    try:
        n = int(variable)
    except:
        return jsonify({
            "status": 400,
            "error": en_errors[60]
        }), 400
    return 0


def invalid_json():
    try:
        request.get_json()
    except:
        return jsonify(
            {"status": 400,
             "error": en_errors[63]
             }
        ), 400
    return 0
