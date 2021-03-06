__author__ = 'verasraul'
from User import User

class UsersManager():
    users = {} #userName

    # def __init__(self, name):
    #     self.name = name

    def get_user(self, name):
        return self.users[name]

    def add_user(self, name):
        # self.name = name
        user = User(name)  #create user
        self.users[name] = user #add user created

    def update_password(self, user_name, account_name, new_password):
        get_user(user_name).updatePassword(account_name, new_password)
