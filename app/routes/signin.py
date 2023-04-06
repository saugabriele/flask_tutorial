from flask import render_template, flash, redirect
from app import app
from models import User
from app.forms import SignInForm
from flask import abort
from werkzeug.security import generate_password_hash


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    user = {"username": "Utente"}
    form = SignInForm()
    if form.validate_on_submit():
        same_email = User.objects(email=form.email.data)
        if len(same_email) > 0:
            abort(403, "Forbidden. Email already in use.")
        else:
            hashpass = generate_password_hash(form.password.data,
                                              method='sha256')
            user = User(email=form.email.data,
                        username=form.username.data,
                        password=hashpass)
        user.save()
        return redirect("/index")
    return render_template('signin.html', title='Sign in', form=form, user=user)