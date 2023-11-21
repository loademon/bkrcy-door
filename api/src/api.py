from db import rd
from app import app
from error import Error


@app.route("/", methods=["GET"])
# how to use page
async def home():
    return "<h1>usage: /user</h1>"


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