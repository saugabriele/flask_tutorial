from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    # instantiate a login form
    user = {'username': 'Gabriele'}
    form = LoginForm()
    if form.validate_on_submit():
        # todo: we will handle this later
        return redirect('/index')
    return render_template('login.html', title='Login', form=form, user=user)
