from flask import render_template, flash, redirect
from app import app
from models import User
from app.forms import SignInForm


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    user = {"username": "Utente"}
    form = SignInForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        user.save()
        return redirect("/index")
    return render_template('signin.html', title='Login', form=form, user=user)