from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import datetime
import os.path


database = SQLAlchemy()
login_manager = LoginManager()


def greet_me():
    return f"Good {['morning', 'morning', 'afternoon', 'evening'][int(datetime.now().hour/6)]}"


def page_not_found(e):
    return render_template('404.html'), 404


def create_database(app):
    file = 'piet.sqlite'
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        database.create_all(app=app)
        print('Created Database!')
