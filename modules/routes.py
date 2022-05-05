from app import app
from flask import render_template, request, redirect, session
from modules.activites import get_activities

from modules.me import get_me
from modules.users import get_users
import sys


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/me", methods=["POST", "GET"])
def me():
    if request.method == "GET":
        return render_template("me.html", me=get_me())


@app.route("/activities", methods=["GET"])
def activities():
    activities = get_activities()
    print(activities, file=sys.stdout)
    return render_template("components/activities.html", activities=activities)


@app.route("/users", methods=["POST", "GET"])
def users():
    if request.method == "GET":
        return render_template("components/users.html", data=get_users())
