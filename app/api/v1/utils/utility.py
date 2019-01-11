def id_generator(ids, key):
    if key in ids.keys():
        ids[key] = ids[key] + 1
        return ids[key]
    ids[key] = 1
    return ids[key]


def meet_up_add_breath(meet_up, id_dictionary):
    if not isinstance(meet_up, dict):
        return 502
    meet_up["id"] = id_generator(id_dictionary, "meet_up")
    meet_up["question"] = []
    meet_up["rsvp"] = {}
    for i in meet_up["user"]:
        meet_up["rsvp"][i] = "null"
    return meet_up



def question_add_breath(question, id_dictionary):
    if not isinstance(question, dict):
        return 502
    question["vote"] = 0
    question["down"] = 0
    question["comment"] = []
    question["id"] = id_generator(id_dictionary, "question")
    return question


def reflect_question(question):
    copy = question.copy()
    if not isinstance(question, dict):
        return 501
    question_feedback = copy
    del question_feedback["vote"]
    del question_feedback["down"]
    del question_feedback["comment"]
    return question_feedback


def reflect_meetup(meet_up):
    copy = meet_up.copy()
    if not isinstance(meet_up, dict):
        return 501
    meetup_feedback=copy
    del meetup_feedback["question"]
    del meetup_feedback["rsvp"]
    return meetup_feedback


def reflect_vote(meet_up,question_index):
    copy = meet_up.copy()
    if not isinstance(meet_up, dict):
        return 501
    meetup_feedback = copy
    meetup_feedback["body"] =meet_up["question"][question_index]["body"]
    meetup_feedback["vote"] = meet_up["question"][question_index]["vote"]
    del meetup_feedback["question"]
    del meetup_feedback["user"]
    return meetup_feedback
