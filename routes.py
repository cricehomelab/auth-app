app = create_app()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Route
@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html", title="Home")

# Login Route
@app.route("/login/", methods=("GET", "POST"), strict_slashes=False )
def login():
    form = login_form()

    return render_template("auth.html", form=form)

# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()

    return render_template("auth.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)