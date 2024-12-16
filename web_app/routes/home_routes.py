# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template
from app.smiski_quiz import Image, display

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")

@home_routes.route("/explore")
def explore():
    print("EXPLORE...")
    return render_template("explore.html")

@home_routes.route("/garden")
def garden():
    print("GARDEN...")
    return render_template("garden.html")