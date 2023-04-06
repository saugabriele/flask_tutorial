from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/my_page')
@login_required
def my_page():
    user = current_user
    return render_template('mypage.html', title='My page', user=user, greeting="Yo")
