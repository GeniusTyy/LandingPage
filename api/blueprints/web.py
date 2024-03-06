from flask import Blueprint, redirect, render_template


web = Blueprint("web", __name__)


@web.route("/")
def home():
    return render_template("home.html", message="Hello word")
