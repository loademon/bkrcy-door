from db import rd
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
    current_user,
)
import asyncio
from secrets import token_hex
from error import Error


@app.route("/", methods=["GET"])
# how to use page
async def home():
    go_to_login_page_button = "<a href='/login'>Go to login page</a>"
    return f"<h1>usage: /user, /user/{{uid}}, /login</h1>{go_to_login_page_button}"


@app.route("/user", methods=["GET"])
# how to use page
async def user():
    return "<h1>usage: /user/{uid}</h1>"


@app.route("/user/<uid>", methods=["GET"])
# getting full user info by id
async def get_user(uid):
    id = f"user:{uid}"
    if await rd.exists(id):
        return await rd.hgetall(id)
    raise Error(f"User {uid} not found")


app.secret_key = token_hex(16)

login_menager = LoginManager()
login_menager.init_app(app)


class User(UserMixin):
    def __init__(self, id, password):
        self.id = id
        self.password = password

    async def get(id):
        passw = await rd.hget(f"account:{id}", "password")
        return User(id, passw)


@login_menager.user_loader
def user_loader(id):
    return User(id, asyncio.run(User.get(id)))


@app.route("/login", methods=["GET"])
async def login():
    # create simple login page with button and form
    page = """
    <form action="/login" method="POST">
        <input type="text" name="id">
        <input type="password" name="password">
        <input type="submit" value="login">
    </form>
    """
    return page


@app.post("/login")
async def login_post():
    id = request.form["id"]
    user = await User.get(id=id)

    if user is None or not check_password_hash(user.password, request.form["password"]):
        return redirect(url_for("login"))

    login_user(user)
    return redirect(url_for("protected"))


@app.route("/protected")
@login_required
async def protected():
    print(current_user)
    return render_template_string("Logged in as: {{ user.id }}", user=current_user)


@app.route("/logout")
async def logout():
    logout_user()
    return "Logged out"


from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)
