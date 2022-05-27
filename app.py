from blueprint.main import main as main_blueprint
from blueprint.auth import auth as auth_blueprint
from flask import Flask
from models import User
from helper import create_database, database as db, greet_me, login_manager as lm, page_not_found
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'f3ab40a06421328cee473372620d19d35968c2419846bb9907ac6e8e182c3d3c'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///piet.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_error_handler(404, page_not_found)

# init SQLAlchemy
db.init_app(app)
create_database(app)

# init login manager
lm.login_view = 'auth.login'
lm.init_app(app)

@lm.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

@app.context_processor
def inject_dict_for_all_templates():
    return dict(greetings=greet_me())

# blueprint for auth routes in our app
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)