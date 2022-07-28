from flask import Blueprint, render_template


yearly = Blueprint('yearly', __name__, template_folder='templates')

@yearly.route('/<year>')
def index(year):
    try:
        if int(year) in [2021, 2022]:
            return render_template('yearly.html', YEAR=year)
    except:
        pass
    return '<h1>404</h1>'
