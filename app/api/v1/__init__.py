from flask import Flask, request, jsonify, Blueprint
from app.api.v1.controller.meetupclass import MeetUp
from app.api.v1.controller.questionclass import Question
from app.api.v1.controller.userclass import User
from app.api.v1.model.database import *
from app.api.v1.controller.rsvpclass import Rsvp
from app.api.v1.utils.utility import meet_up_add_breath, question_add_breath, reflect_meetup, reflect_question, \
    id_generator, reflect_vote, user_add_breath, validate_user_login_details
from app.api.v1.utils.error_file import en_errors

application = Flask(__name__)
blueprint = Blueprint("name", __name__, url_prefix="/api/v1")
application.register_blueprint(blueprint)


# @application.route("/meetups", methods=["get"])
def meetup():
    responses = []
    for i in meet_ups:
        responses.append(reflect_meetup(i))
    return jsonify(responses)


# @application.route("/meetups", methods=["post"])
def post_meet_up():
    if invalid_json():
        return invalid_json()
    final = meet_up_add_breath(request.get_json(), ids)
    if final == 31131:
        return jsonify(
            {
                "error": en_errors[70]
            }
        )
    test = MeetUp(final)
    error = test.self_validate()
    if not error:
        meet_ups.append(final)
        return jsonify(reflect_meetup(final))
    return jsonify({
        "error": en_errors[error]
    })


# @application.route("/meetups/<meet_up_id>", methods=["get"])
def meet_up_specific(meet_up_id):
    if invalid_id(meet_up_id):
        return invalid_id(meet_up_id)
    for i in meet_ups:
        buffer = MeetUp(i)
        if buffer.get_meet_up_id() == int(meet_up_id):
            return jsonify(reflect_meetup(i))
    return jsonify({
        "error": en_errors[69]
    })


# @application.route("/question", methods=["post"])
def post_question():
    if invalid_json():
        return invalid_json()
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


# @application.route("/question/<question_id>/upvote", methods=["patch"])
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


# @application.route("/question/<question_id>/downvote", methods=["patch"])
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


# @application.route("/meetups/<meetup_id>/rsvp", methods=["post"])
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
                m["rsvp"][request.get_json()["userid"]] = request.get_json()["rsvp"]
                return jsonify({
                    "status": 201,
                    "message": en_errors["cor-rsvp"]
                })
        return jsonify(
            {
                "status": 00,
                "error": en_errors[59]
            }
        )
    return jsonify(en_errors[error])


# @application.route("/look")
def remember():
    print(meet_ups)
    return "done"


# @application.route("/signup", methods=["post"])
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
                )
            if sample.get_email() == tempUser.get_email():
                return jsonify(
                    {
                        "errror": en_errors[802]
                    }
                )
        users.append(tempUser.get_data())
        return jsonify(
            {"status": 201,
             "data": tempUser.get_data()
             }
        )
    return jsonify({
        "error": en_errors[error]
    })


# @application.route("/login", methods=["post"])
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
                        "data": en_errors[73]
                    })
            if "username" in data.keys():
                if temp_user.get_user_name() == data["username"] and temp_user.get_password() == request.get_json()[
                    "password"]:
                    login_user.append(temp_user.get_id())
                    return jsonify({
                        "status": 201,
                        "data": en_errors[73]
                    })
    if validate_user_login_details(request.get_json()) != 0:
        return jsonify({
            "error": en_errors[validate_user_login_details(request.get_json())]
        })
    return jsonify({
        "error": en_errors[711]
    })


single_route_name_server = {
    "meetups": {
        "method": ["POST", "GET"]
    },
    "question": {
        "method": ["POST"]
    },
    "signup": {
        "method": ["POST"]
    },
    "login": {
        "method": ["POST"]
    }
}

Double_route_name_server = {
    "meetups": {
        "method": "GET"
    }
}

Three_route_name_server = {
    "question": {
        "method": "PATCH",
        "second_additions": ["*"],
        "third_addition": ["upvote", "downvote"]
    },
    "meetups": {
        "method": "POST"
    }
}

allowed_methods = ["POST", "GET", "PATCH", "PUT", "DELETE", "COPY",
                   "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK",
                   "UNLOCK", "PROPFIND", "VIEW"]


@application.route("/<location>", methods=allowed_methods)
def single_route_consumer(location):
    if not location in single_route_name_server.keys():
        return jsonify({
            "error": en_errors[74]
        })
    if not request.method in single_route_name_server[location]["method"]:
        return jsonify(
            {
                "error": en_errors[67] + request.method + en_errors[68]
            }
        )
    if location == "meetups" and request.method == "GET":
        return meetup()
    if invalid_json():
        return invalid_json()
    if request.method == "POST":
        if location == "meetups":
            return post_meet_up()
        if location == "signup":
            return sign_up()
        if location == "login":
            return login()
        if location == "question":
            return post_question()
    return jsonify({
        "status": 00,
        "error": en_errors[66]
    })


@application.route("/<first>/<second>", methods=allowed_methods)
def double_route_consumer(first, second):
    invalid_id(second)
    if not first in Double_route_name_server.keys():
        return jsonify({
            "status": 00,
            "error": en_errors[65]
        }
        )
    if not request.method in Double_route_name_server[first]["method"]:
        return jsonify(
            {
                "status": 00,
                "error": en_errors[64]
            }
        )
    return meet_up_specific(second)


@application.route("/<first_route>/<second_route>/<third_route>", methods=allowed_methods)
def three_route_consumer(first_route, second_route, third_route):
    if third_route not in ["rsvp", "upvote", "downvote"]:
        return jsonify({
            "status": 00,
            "error": en_errors[61]
        })
    if not first_route in Three_route_name_server:
        return jsonify({
            "status": 00,
            "error": en_errors[74]
        })
    if request.method == "PATCH":
        if third_route == "upvote":
            return upvote(second_route)
        if third_route == "downvote":
            return down_vote(second_route)
    if request.method == "POST":
        return post_rsvp(second_route)
    return jsonify({
        "status": 00,
        "error": en_errors[62]
    })


@application.route("/", methods=allowed_methods)
def greeting_route():
    return jsonify(
        {
            "data": "questioner"
        }
    )


def create_app():
    return application


def invalid_id(variable):
    try:
        n = int(variable)
    except:
        return jsonify({
            "error": en_errors[60]
        })
    return 0


def invalid_json():
    try:
        request.get_json()
    except:
        return jsonify(
            {
                "error": en_errors[63]
            }
        )
    return 0
