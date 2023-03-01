from wtforms import (
    StringField, 
    PasswordField, 
    BooleanField,
    IntegerField,
    DateField,
    TextAreaField,
    RadioField,
    ValidationError,
    validators,
)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp, Optional
import email_validator
from flask_login import current_user
from models import User

class login_form(FlaskForm):
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    # Placeholder labels to enable form rendering
    username= StringField(
        validators=[Optional()]
    )

class register_form(FlaskForm):
    first_name = StringField(
        validators=[
            InputRequired(),
            Length(1, 140, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z]+$",
                0,
                "first names must only have letters.",
            ),
        ]
    )
    last_name = StringField(
        validators=[
            InputRequired(),
            Length(1, 140, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z]+$",
                0,
                "Usernames must only have letters.",
            ),
        ]
    )
    username = StringField(
        validators=[
            InputRequired(),
            Length(1, 140, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z0-9]+$",
                0,
                "Usernames must only have letters and numbers.",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(8, 72)])
    cpwd = PasswordField(
        validators=[
            InputRequired(),
            Length(8,72),
            EqualTo("pwd", message="Passwords must match!") # TODO: not working right now
        ]
    )
    is_admin = RadioField('Is user an admin?', choices=[("admin", 1), ("user", 0)])
    is_active = RadioField('Is user active?', choices=[("Active", 1), ("Inactive", 0)])

    # End Register Form.

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email already registered!")

    def validate_uname(self, uname):
        if User.query.filter_by(username=uname.data).first():
            raise ValidationError("Username already taken!")