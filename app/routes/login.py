from flask import render_template, flash, redirect, url_for, abort
from app import app
from app.forms import LoginForm
from models import User
from werkzeug.security import check_password_hash
from flask_login import login_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    # instantiate a login form
    user = {'username': 'Gabriele'}
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data)

        if len(user) == 1:
            if check_password_hash(user[0].password, form.password.data):
                login_user(user[0])
                return redirect(url_for('index'))
        else:
            abort(404, "User not found. Please register.")
    return render_template('login.html', title='Login', form=form, user=user)
