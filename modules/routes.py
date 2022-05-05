from app import app
from flask import render_template, request, redirect, session


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
