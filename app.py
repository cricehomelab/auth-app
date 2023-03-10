from flask import Flask
from flask_bcrypt import  Bcrypt

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.secret_key = '59142bafb5d08b1e10730c508e2cdd70a5f1f35b99e15221'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    return app