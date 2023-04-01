from app import app
from flask import render_template


@app.route('/my_page')
def my_page():
    user = {'username': 'Gabriele'}
    return render_template('mypage.html', title='My page', user=user)
