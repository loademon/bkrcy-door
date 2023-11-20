from db import rd
from app import app, jsonify
from error import Error


@app.errorhandler(Error)
def handle_error(error: Error):
    response = jsonify({"error": error.message})
    response.status_code = 404
    return response

@app.route("/user/<uid>", methods=["GET"])
async def get_user(uid):
    id = f"user:{uid}"
    if await rd.exists(id):
        user = await rd.hgetall(id)
        return user
    raise Error(f"User {uid} not found")


app.run(debug=True, threaded=True)
