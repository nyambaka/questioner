from flask import Flask ,request ,jsonify

from app.api.v1.controller.meetupclass import MeetUp
from app.api.v1.controller.questionclass import Question
from app.api.v1.model.database import *
from app.api.v1.utils.utility import meet_up_add_breath, question_add_breath ,reflect_meetup


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


@app.route("/meetup", methods=["post"])
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


if __name__ == '__main__':
    app.run()
