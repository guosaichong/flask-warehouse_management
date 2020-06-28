from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from models import User, query_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json

app = Flask(__name__)
app.secret_key = '1234567'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = '请登录'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id

        return curr_user


@app.route('/')
@login_required
def index():
    return 'Logged in as: %s' % current_user.get_id()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get("psw")
        user = query_user(username)
        if user is not None and generate_password_hash(request.form['password']) == user['password']:

            curr_user = User()
            curr_user.id = user_id

            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)

            return redirect(url_for('index'))

        flash('Wrong username or password!')

    # GET 请求
    return render_template('login.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get("uname")
    password = request.form.get("psw")
    repet_password = request.form.get("repet_psw")
    print(username, password, repet_password)
    if password==repet_password:
        password=generate_password_hash(password)
        #保存用户名和密码到数据库
        pass
    else:
        pass
    return {"success": 0}


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'


def load_from_json():
    if os.path.exists("db.json"):
        json_data = open("db.json", "r").read()
        return json.loads(json_data)
    else:
        return []


def save_user_to_json(user_info):
    user_list = load_user()
    user_list.append(user_info)
    with open("./users.json", "w") as f:
        f.write(json.dumps(user_list,ensure_ascii=False,indent=2))


def load_user():
    if os.path.exists("./user.json"):
        return json.loads(open("./users.json").read())
    else:
        return []


if __name__ == '__main__':
    app.run(debug=True)
