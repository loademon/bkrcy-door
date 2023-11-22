import auth
from db import rd
from app import app, asgi_app
from error import Error


@app.route("/")
# how to use page
def home():
    go_to_login_page_button = "<a href='/login'>Go to login page</a>"
    return f"<h1>usage: /user, /user/{{uid}}, /login</h1>{go_to_login_page_button}"


@app.route("/user")
# how to use page
def user():
    return "<h1>usage: /user/{uid}</h1>"


@app.route("/user/<uid>")
# getting full user info by id
def get_user(uid):
    id = f"user:{uid}"
    if rd.exists(id):
        return rd.hgetall(id)
    raise Error(f"User {uid} not found")


