from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def check_pwd(self, pwd):  # 验证密码
        return check_password_hash(self.pwd, pwd)
users = [
    {'username': 'Tom', 'password': '111111'},
    {'username': 'Michael', 'password': '123456'}
]

def query_user(user_id):
    for user in users:
        if user_id == user['user_id']:
            return user
