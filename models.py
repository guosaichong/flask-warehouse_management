from flask_login import UserMixin


class User(UserMixin):
    pass

users = [
    {'username': 'Tom', 'password': '111111'},
    {'username': 'Michael', 'password': '123456'}
]

def query_user(username):
    for user in users:
        if username == user['username']:
            return user
