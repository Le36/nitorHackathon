from app import app
from flask import render_template, request, redirect, session
from modules.activites import get_activities

from modules.me import get_me
from modules.users import get_users
from modules.coordinates import get_coordinates
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


@app.route("/users/<string:user_id>", methods=["POST", "GET"])
def user(user_id):
    if request.method == "GET":
        return render_template(
          "components/user.html", 
          users=get_users(), 
          coordinates=get_coordinates(),
          user_id=user_id
          )

@app.route("/activities/<string:activity_id>", methods=["POST", "GET"])
def activity(activity_id):
    if request.method == "GET":
        return render_template(
          "components/activity.html", 
          users=get_users(), 
          activity_id=activity_id
          )
