import auth
from json import dumps, loads
from db import rd
from app import (
    app,
    request,
    asgi_app,
    login_required,
    flash,
    redirect,
    url_for,
    render_template,
)
from error import Error
from utils import create_page, Markup


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/user")
@login_required
def user():
    flash_messages_html, page = create_page(
        search=rd.smembers("doors"), type="door_access"
    )

    return render_template(
        "user_form.html", doors=page, flash_messages=flash_messages_html
    )


@app.route("/delete")
@login_required
def delete():
    flash_messages_html, page = create_page(search=rd.scan_iter("user:*"), type="user")

    return render_template(
        "delete_form.html", users=page, flash_messages=flash_messages_html
    )


@app.route("/user/<uid>")
def get_user(uid):
    id = f"user:{uid}"
    if rd.exists(id):
        data = rd.hgetall(id)
        data["doors"] = loads(data["doors"])
        return data
    raise Error(f"User {uid} not found")


@app.route("/user", methods=["POST"])
@login_required
def post_user():
    data = request.form
    if rd.exists(f"user:{data['uid']}"):
        flash("User edited successfully", "success")
    else:
        flash("User created successfully", "success")

    rd.hset(
        name=f"user:{data['uid']}",
        mapping={
            "name": data["name"],
            "school_number": data["school_number"],
            "expiration_date": data["expiration_date"],
            "doors": dumps(data.getlist("door_access")),
        },
    )
    return redirect(url_for("user"))


@app.route("/delete/", methods=["POST"])
@login_required
def delete_user():
    users = request.form.getlist("user")

    for uid in users:
        if rd.exists(uid):
            rd.delete(uid)
    flash(f"User/s deleted successfully", "success")
    return redirect(url_for("delete"))


@app.route("/purge/<uid>")
@login_required
def purge_door_access(uid):
    users = rd.scan_iter("user:*")
    for user in users:
        doors = loads(rd.hget(user, "doors"))
        if uid in doors:
            doors.remove(uid)
            rd.hset(user, "doors", dumps(doors))
    return {"message": "success"}
