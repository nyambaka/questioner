def id_generator(ids, key):
    if key in ids.keys():
        ids[key] = ids[key] + 1
        return ids[key]
    ids[key] = 1
    return ids[key]


def meet_up_add_breath(meet_up, id_dictionary):
    if not isinstance(meet_up, dict):
        return 501
    meet_up["id"] = id_generator(id_dictionary, "meet_up")
    meet_up["question"] = []
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
        return 503
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
    return meetup_feedback