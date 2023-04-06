from app import app
from flask import url_for, redirect
from flask_login import login_required, logout_user


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
