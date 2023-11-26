from app import (
    app,
    LoginManager,
    UserMixin,
    redirect,
    url_for,
    request,
    login_user,
    logout_user,
    login_required,
    check_password_hash,
    generate_password_hash,
    render_template_string,
    render_template,
    current_user,
    Markup,
)
from db import rd
from secrets import token_hex

app.secret_key = token_hex(16)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, id, password):
        self.id = id
        self.password = password

    @staticmethod
    def get(id):
        passw = rd.hget(f"account:{id}", "password")
        if passw:
            return User(id, passw)
        return None


@login_manager.user_loader
def user_loader(id):
    return User.get(id=id)


@app.route("/login")
def login():
    return render_template("login.html")


@app.post("/login")
def login_post():
    id = request.form["id"]
    user = User.get(id=id)

    if user is None or not check_password_hash(user.password, request.form["password"]):
        return redirect(url_for("login"))

    login_user(user)
    return redirect(url_for("protected"))


@app.route("/protected")
@login_required
def protected():
    return render_template("protected.html")


@app.route("/logout")
def logout():
    logout_user()
    return "Logged out"
