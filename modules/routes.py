from app import app
from flask import render_template, request, redirect, session
from modules.activites import get_activities
from modules.closest import get_closest

from modules.me import get_me
from modules.users import get_users
from modules.coordinates import get_coordinates, get_friend_coordinates, get_own_coords, get_distance
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


@app.route("/secret", methods=["POST", "GET"])
def secret():
    if request.method == "GET":
        return render_template("components/secret.html")


@app.route("/activities", methods=["GET"])
def activities():
    return render_template("components/activities.html", activities=get_activities())


@app.route("/map", methods=["GET"])
def map_markers():
    return render_template("map.html", coords=get_coordinates(), me=get_me())


@app.route("/closest", methods=["GET"])
def closest_restaurants():
    coords = []
    own_coords = get_own_coords()
    own_lat = float(own_coords.split("%2C")[0])
    own_lon = float(own_coords.split("%2C")[1])
    for place in get_closest(get_own_coords()):
        place_lat = float(place["lat"])
        place_lon = float(place["lon"])
        distance = get_distance(own_lat, own_lon, place_lat, place_lon)
        coords.append((place["tags"]["name"], str(distance)))

    return render_template("closest.html", places=coords)


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


@app.route("/find-friend", methods=["GET"])
def find_collegue():
    distances = get_friend_coordinates()
    distances.sort(key=lambda a: a[1])

    print(distances, file=sys.stdout)

    return render_template("components/find-friend.html", distances=distances)


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
