from app import db
from flask import Flask, Blueprint
from flask_login import LoginManager

app = Flask(__name__)
app.debug = True
app.secret_key = 'sljsdkjdslkjsdflkj29037ij'

from app.routes import auth, main

app.register_blueprint(auth.auth)
app.register_blueprint(main.main)

db.setup_db(app)

from app.models import User

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)