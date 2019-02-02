from flask import Flask, request, jsonify, Blueprint
from app.api.v1.controller.meetupclass import MeetUp
from app.api.v1.controller.questionclass import Question
from app.api.v1.model.database import *
from app.api.v1.controller.front_controller import FrontController
from app.api.v1.controller.rsvpclass import Rsvp
from app.api.v1.utils.error_file import en_errors
from datetime import datetime
from app.api.v1.controller.get_front_controller import GetFrontController
from app.api.v1.controller.get_question import GetQuestion
from app.api.v1.controller.get_meetup import GetMeetup
from app.api.v1.controller.abs_patch import Patch
from app.api.v1.controller.userclass import User
from app.api.v1.controller.login import Login

blueprint = Blueprint('blueprint', __name__)


@blueprint.route("/meetups", methods=["get"])
def meetup():
    buffer = GetFrontController(GetMeetup, meet_ups)
    return buffer.get().show()


@blueprint.route("/meetups", methods=["post"])
def post_meet_up():
    if invalid_json():
        return invalid_json()
    test = FrontController(MeetUp, request.get_json())
    return test.post(ids, meet_ups)


@blueprint.route("/meetups/<meet_up_id>", methods=["get"])
def meet_up_specific(meet_up_id):
    buffer = GetFrontController(GetMeetup, meet_ups)
    return buffer.get(meet_up_id).show()


@blueprint.route("/question", methods=["post"])
def post_question():
    if invalid_json():
        return invalid_json()
    test = FrontController(Question, request.get_json())
    return test.post(ids, meet_ups)


@blueprint.route("/question", methods=["get"])
def get_question():
    buffer = GetFrontController(GetQuestion, meet_ups)
    return buffer.get().show()


@blueprint.route("/question/<question_id>/upvote", methods=["patch"])
def upvote(question_id):
    if invalid_id(question_id):
        return invalid_id(question_id)
    buffer = Patch(meet_ups)
    return buffer.up_vote(question_id).show()


@blueprint.route("/question/<question_id>/downvote", methods=["patch"])
def down_vote(question_id):
    if invalid_id(question_id):
        return invalid_id(question_id)
    buffer = Patch(meet_ups)
    return buffer.down_vote(question_id).show()


@blueprint.route("/meetups/<meetup_id>/rsvp", methods=["post"])
def post_rsvp(meetup_id):
    if invalid_json():
        return invalid_json()
    if invalid_id(meetup_id):
        return invalid_id(meetup_id)
    buffer= FrontController(Rsvp,request.get_json())
    return buffer.post(ids,meet_ups)


@blueprint.route("/look")
def remember():
    return jsonify(
        {
            "status": 200,
            "data": meet_ups
        }
    ),200


@blueprint.route("/signup", methods=["post"])
def sign_up():
    if invalid_json():
        return invalid_json()
    buffer = FrontController(User,request.get_json())
    return buffer.post(ids,users)


@blueprint.route("/login", methods=["post"])
def login():
    if invalid_json():
        return invalid_json()
    buffer = Login(request.get_json(),users)
    buffer.new_display()
    buffer.login_user()
    result = buffer.get_display()
    return result.render_internal_error()

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
