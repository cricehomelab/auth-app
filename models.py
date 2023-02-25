from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(140), unique=False, nullable=False)
    last_name = db.Column(db.String(140), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)
    password_date = db.Column(db.Integer, nullable=False, unique=False) # Unix time for date password was last set.
    require_password_set = db.Column(db.Integer, nullable=False, unique=False) # require password reset on next login. 
    is_admin = db.Column(db.Integer, nullable=False, unique=False) # determines if user is an admin or not.
    is_active = db.Column(db.Integer, nullable=False, unique=False) # determines if user is able to login.

    def __repr__(self):
        return '<User %r>' %self.username