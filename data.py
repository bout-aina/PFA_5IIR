# you can use: class User(Usermixin)
"""
UserMixin pre-defines these attributes for your User class:
def is_authenticated():
    ...
def is_active():
    ...
def is_anonymous():
    ...
def get_id():
    ...
"""


# or you can just define these attributes yourself
class User():
    def __init__(self, id, username, active=True):
        self.id = id
        self.username = username
        self.active = active

    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        # return self.active
        # for demo i just return True
        return True

    def is_authenticated(self):
        # for demo i just return True
        return True

    def get_id(self):
        # if you do not use Usermixin, this is important
        # user_loader load_user(id) uses this get_id attribute to load the id
        return self.id


# create local database of sample users
# Key are user id's : Value are User objects
USERS = {
    "123123": User("123123", "user1"),

}


def confirmUserLogin(id, password):
    # check local db USERS for the id
    if USERS.get(sso):
        # get the user object (key's value)
        user = USERS.get(id)
        # check password
        if user.password == password:
            # entered password matches database password
            response = {"status": True, "message": "Login Successfull!"}
            return response
        else:
            # entered password DOES NOT match database password
            response = {"status": False, "message": "Wrong password, please try again."}
            return response
    else:
        # user does not exist
        response = {"status": False, "message": "User does not exist, please try again."}
        return response