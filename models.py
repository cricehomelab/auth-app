from app import db
from flask_login import UserMixin

# DB model for a User account. 
class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(140), unique=False, nullable=False)       # (String) First name of user.
    last_name = db.Column(db.String(140), unique=False, nullable=False)        # (String) Last name of user.
    email = db.Column(db.String(120), unique=True, nullable=False)             # (String) Email address of user.
    username = db.Column(db.String(140), unique=True, nullable=True)           # (String) Username for user. NOTE: can change nullable to False to make this field required.
    pwd = db.Column(db.String(300), nullable=False, unique=True)               # (String) Hashed user password.
    password_date = db.Column(db.Integer, nullable=False, unique=False)        # (Integer) Unix time for date password was last set.
    last_login = db.Column(db.Integer, nullable=False, unique=False)           # (Integer) Last time in Unix time that user logged in.
    require_password_set = db.Column(db.Integer, nullable=False, unique=False) # (Integer 0 or 1) Require password reset on next login.
    is_admin = db.Column(db.Integer, nullable=False, unique=False)             # (Integer 0 or 1) Determines if user is an admin or not.
    is_active = db.Column(db.Integer, nullable=False, unique=False)            # (Integer 0 or 1) Determines if user is active or not.

    def __repr__(self):
        return '<User %r>' %self.username