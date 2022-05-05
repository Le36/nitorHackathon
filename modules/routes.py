from app import app
from flask import render_template, request, redirect, session

from modules.me import get_me


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
    return render_template("components/activities.html")
