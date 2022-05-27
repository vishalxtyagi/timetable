from sched import scheduler
from flask import Blueprint, jsonify, render_template, request
from flask_login import login_required, current_user
from timetable import Schedule
from pathlib import Path
import csv, os

main = Blueprint('main', __name__)
schedule = Schedule()
base_dir = Path(__file__).parent.resolve()


def get_recommendations(day_name, lecture, subject):

    day_name = day_name.lower()
    Teachers = []
    if day_name == 'monday':
        with open(os.path.join(base_dir, 'dataset', 'monday.csv'), 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
                print(row)
    elif day_name == 'tuesday':
        with open(os.path.join(base_dir, 'dataset', 'tuesday.csv'), 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
                print(row)
    elif day_name == 'wednesday':
        with open(os.path.join(base_dir, 'dataset', 'wednesday.csv'), 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
                print(row)
    elif day_name == 'thursday':
        with open(os.path.join(base_dir, 'dataset', 'thursday.csv'), 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
                print(row)
    elif day_name == 'friday':
        with open(os.path.join(base_dir, 'dataset', 'friday.csv'), 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
                print(row)
    
    possible_sub = {}
    no_class = []
    sub_possible_sub = []
    sub_no_class = []

    ab_lect = int(lecture)
    subject = subject.lower()


    # first priority (if subsequent lecture is free too)
    for i in Teachers:
        count = 0
        if i[ab_lect] != '1' and i[ab_lect-1] != '1' and i[ab_lect+1] != '1':             # looks for the possible substitutes
            possible_sub[i[0]] = i[-1]
            for j in i:                 # counts the total number of free periods
                if j == '0':
                    count += 1
            no_class.append(count)

    # second priority
    if possible_sub == {}:
        for i in Teachers:
            count = 0
            if i[ab_lect] == '0':
                possible_sub[i[0]] = i[-1]
                for j in i:
                    if j == '0':
                        count += 1
                no_class.append(count)

    print(possible_sub)  # prints the possible substitutes
    print(no_class)     # prints the total number of free periods

    result = []
    # to see if the teacher specializes in the same subject
    for i, (key, value) in enumerate(possible_sub.items()):
        count = 0
        if value == subject:
            sub_possible_sub.append(key)
            sub_no_class.append(no_class[i])
    if sub_possible_sub != []:
        suited_teacher = max(sub_no_class)  # gives the teacher with the most amount of free time
        print("The recommended teacher would be:")
        for i in range(len(sub_possible_sub)):
            if no_class[i] == suited_teacher:
                result.append(sub_possible_sub[i])  # prints the teacher to that index

    # if the possible candidates do not teach the preferred subject
    else:
        suited_teacher = max(no_class)  # gives the teacher with the most amount of free time
        print("The recommended teacher would be:")
        for i, (key, value) in enumerate(possible_sub.items()):
            if no_class[i] == suited_teacher:
                result.append(key)  # prints the teacher to that index

    return result, possible_sub

@main.route('/')
@login_required
def home():
    return render_template(
        'home.html',
        name=current_user.name,
        teachers=schedule.get_all_teachers()
    )


@main.route('/find-substitute-teachers', methods=['GET', 'POST'])
@login_required
def substitute():
    if request.method == "GET":
        return render_template(
            'substitute.html',
            name=current_user.name,
        )
    
    lecture = request.form.get('lecture')
    subject = request.form.get('subject')
    day = request.form.get('day')
    recommend,pos = get_recommendations(day,lecture,subject)
    return render_template(
        'result.html',
        results=recommend,
        poss=pos
    )


@main.route('/about/<teacher>')
@login_required
def about(teacher):
    return render_template('about.html', teacher=teacher)