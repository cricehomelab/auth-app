# Imports from established libraries.
from datetime import timedelta
import time

from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    url_for,
    session
)

from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError, 
    InterfaceError,
    InvalidRequestError,
)

from werkzeug.routing import BuildError

# imports from files that we wrote for this.
from app import create_app, db, login_manager, bcrypt
from models import User
from forms import login_form, register_form


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app = create_app()

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html",title="Home")


@app.route("/login/", methods=("GET", "POST"), strict_slashes=False )
def login():
    form = login_form()
    print(form)

    if form.validate_on_submit():
        try:
            print(f"Email being searched for: {form.email.data}")
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Invailid Username or password!", "danger")
        except Exception as e:
            flash(e, 'danger')

    return render_template("auth.html",
    form=form,
    text="Login",
    title="Login",
    btn_action="Login"
    )



# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()
    if form.validate_on_submit():
        print("Hello")
        try:
            first_name = form.first_name.data
            print(first_name)
            last_name = form.last_name.data
            print(last_name)
            username = form.username.data
            print(username)
            email = form.email.data
            print(email)
            pwd = form.pwd.data
            print(pwd)
            cpwd = form.cpwd.data
            print(cpwd)

            newuser = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                pwd=bcrypt.generate_password_hash(pwd),
                password_date=time.time(),
                last_login=time.time(),
                require_password_set=0,
                is_admin=1,  # TODO: get this in the form so we don't hardcode this
                is_active=1, # TODO: get this in the form so we don't hardcode this
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Successfully created", "success")
            return redirect(url_for("login"))
        
        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something Went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists!", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "danger")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured", "danger")
    else:
        print(form.validate_on_submit())
    return render_template("auth.html", 
        form=form,
        text="Create Account",
        title="Register",
        btn_action="Register account"
    )

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)