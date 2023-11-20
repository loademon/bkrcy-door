from db import rd
from app import app, asgi_app, jsonify

from error import Error


@app.route("/user/<uid>", methods=["GET"])
async def get_user(uid):
    id = f"user:{uid}"
    if await rd.exists(id):
        user = await rd.hgetall(id)
        return user
    raise Error(f"User {uid} not found")
