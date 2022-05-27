from flask import Blueprint, render_template
from flask_login import login_required, current_user
from timetable import Schedule

main = Blueprint('main', __name__)
schedule = Schedule()

@main.route('/')
@login_required
def home():
    return render_template(
        'home.html',
        name=current_user.name,
        teachers=schedule.get_all_teachers()
    )


@main.route('/find-substitute-teachers')
@login_required
def substitute():
    return render_template(
        'substitute.html',
        name=current_user.name,
    )


@main.route('/about/<teacher>')
@login_required
def about(teacher):
    return render_template('about.html', teacher=teacher)