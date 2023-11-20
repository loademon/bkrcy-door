from db import rd
from app import app, asgi_app, jsonify

from error import Error

@app.route("/user", methods=["GET"])
# how to use page
async def user():
    return "Usage: /user/<id>"


@app.route("/user/<uid>", methods=["GET"])
# getting full user info by id
async def get_user(uid):
    id = f"user:{uid}"
    if await rd.exists(id):
        return await rd.hgetall(id)
    raise Error(f"User {uid} not found")


app.run(port=8000)
