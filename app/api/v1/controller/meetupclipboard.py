def meetupAddbreath(meetup):
    if not isinstance(meetup, dict):
        return 501
    meetup["id"] = id_generator("meetup")
    meetup["question"] = []
    return meetup


incoming = {
    "user": [1, 2, 3]
}

incoming2 = {
    "label": "Group Diamond",
    "user": [1, 2, 3]
}

incominguser = {
    "id": 1,
    "username": "nelson",
    "firstname": "nelson",
    "lastname": "nyambaka",
    "othername": "nyambaka",
    "password": "kingking",
    "email": "nelsonnyambaka@gmail.com",
    "registered": "2019-01-20",
    "isadmin": True,
    "phonenumber": "0700741837"

}

testuser = User(incominguser)

error = testuser.selfValidate()
if not error:
    print("succcess")
else:
    print(error)

# if  meetupAddbreath(incoming) :
# 	temp=meetup(meetupAddbreath(incoming))
# 	result= temp.selfValidate()
# 	if not result:
# 		meetups.append(temp.getData())
# 	print(result)


# print(meetups)