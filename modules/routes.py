from app import app
from flask import render_template, request, redirect, session
from modules.activites import get_activities

from modules.me import get_me
from modules.users import get_users
from modules.coordinates import get_coordinates
from modules.toFlights import get_toFlights
from modules.fromFlights import get_fromFlights
from modules.hacktivities import get_hacktivities
from modules.randomInt import get_randomInt
import sys


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/me", methods=["POST", "GET"])
def me():
    if request.method == "GET":
        return render_template(
            "me.html",
            hacktivities=get_hacktivities(),
            task_id=get_randomInt(),
            me=get_me()
        )


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
            activities=get_activities(),
            activity_id=activity_id
        )


@app.route("/flights", methods=["POST", "GET"])
def toFlights():
    if request.method == "GET":
        return render_template(
            "components/flights.html",
            toFlights=get_toFlights(),
            fromFlights=get_fromFlights()
        )


@app.route("/flights/<string:flight_id>", methods=["POST", "GET"])
def toFlight(flight_id):
    if request.method == "GET":
        return render_template(
            "components/flight.html",
            users=get_users(),
            flight_id=flight_id
        )


@app.errorhandler(404)
def error404(error):
    return render_template("error.html"), 404


@app.errorhandler(500)
def error500(error):
    return render_template("error.html"), 500


@app.errorhandler(502)
def error502(error):
    return render_template("error.html"), 502


@app.errorhandler(503)
def error503(error):
    return render_template("error.html"), 503
