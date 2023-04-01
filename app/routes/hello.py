from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gabriele'}
    students = [
        {'name': 'A', 'id': 1},
        {'name': 'C', 'id': 111},
    ]
    return render_template('index.html', title='Home', user=user, students=students, greeting="Yo")
