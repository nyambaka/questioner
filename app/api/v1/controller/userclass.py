class User:

    def __init__(self, data):
        self.data = data

    def is_set(self, key=""):
        return key in self.data.keys()

    def type_check(self, key, type_claim):
        return isinstance(self.data[key], type_claim)

    def get_id(self):
        if not self.is_set("id"):
            return 401
        return self.data['id']

    def set_id(self, new_id):
        if not isinstance(new_id, str):
            return 402
        self.data["id"] = new_id
        return self

    def get_firstname(self):
        if not self.is_set("firstname"):
            return 403
        return self.data["firstname"]

    def set_first_name(self, new_firstname):
        if not isinstance(new_firstname, str):
            return 404
        self.data["firstname"] = new_firstname
        return self

    def get_last_name(self):
        if not self.is_set("lastname"):
            return 405
        return self.data["lastname"]

    def set_last_name(self, new_lastname):
        if not isinstance(new_lastname, str):
            return 406
        self.data["lastname"] = new_lastname
        return self

    def get_other_name(self):
        if not self.is_set("othername"):
            return 407
        return self.data["othername"]

    def set_other_name(self, new_othername):
        if not isinstance(new_othername, str):
            return 408
        self.data["othername"] = new_othername

    def get_email(self):
        if not self.is_set("email"):
            return 409
        return self.data["email"]

    def set_email(self, new_email):
        if not isinstance(new_email, str):
            return 410
        self.data["email"] = new_email

    def get_phone_number(self):
        if not self.is_set("phonenumber"):
            return 411
        return self.data["phonenumber"]

    def set_phone_number(self, new_phonenumber):
        if not isinstance(new_phonenumber, str):
            return 412
        self.data["phonenumber"] = new_phonenumber
        return self

    def get_user_name(self):
        if not self.is_set("username"):
            return 413
        return self.data["username"]

    def set_user_name(self, new_username):
        if not isinstance(new_username, str):
            return 414
        self.data["username"] = new_username
        return self

    def get_registered(self):
        if not self.is_set("registered"):
            return 415
        return self.data["registered"]

    def set_registered(self, new_registered):
        if not isinstance(new_registered, str):
            return 416
        self.data["registered"] = new_registered
        return self

    def get_is_admin(self):
        if not self.is_set("isadmin"):
            return 417
        return self.data["isadmin"]

    def set_is_admin(self, new_isadmin):
        if not isinstance(new_isadmin, int):
            return 418
        self.data["isadmin"] = new_isadmin
        return self

    def get_password(self):
        if not self.is_set("password"):
            return 419
        return self.data["password"]

    def set_password(self, new_password):
        if not isinstance(new_password, str):
            return 420
        self.data["password"] = new_password
        return self

    def get_data(self):
        return self.data

    def self_validate(self):
        if not isinstance(self.data, dict):
            return 419
        if not self.is_set("id"):
            return 401
        if not self.type_check("id", int):
            return 402
        if not self.is_set("firstname"):
            return 403
        if not self.type_check("firstname", str):
            return 404
        if not self.is_set("lastname"):
            return 405
        if not self.type_check("lastname", str):
            return 406
        if not self.is_set("othername"):
            return 407
        if not self.type_check("othername", str):
            return 408
        if not self.is_set("email"):
            return 409
        if not self.type_check("email", str):
            return 410
        if not self.is_set("phonenumber"):
            return 411
        if not self.type_check("phonenumber", str):
            return 412
        if not self.is_set("username"):
            return 413
        if not self.type_check("username", str):
            return 414
        if not self.is_set("registered"):
            return 415
        if not self.type_check("registered", str):
            return 416
        if not self.is_set("isadmin"):
            return 417
        if not self.type_check("isadmin", int):
            return 418
        if not self.is_set("password"):
            return 419
        if not self.type_check("password", str):
            return 420
        return 0

# sampleuser={
# 	"id":1,
# 	"firstname":"nelson",
# 	"lastname":"nyambaka",
# 	"othername":"nyambaka",
# 	"email":"nelsonnyambaka@gmail.com",
# 	"phonenumber":"0700741837",
# 	"username":"nelly",
# 	"registered":"2018-01-20",
# 	"isadmin":True
# }

# test=User(sampleuser)
# result=test.selfValidate()
# print(result)
