# routes/api.py
from flask import Blueprint, jsonify, render_template
from datetime import datetime

api = Blueprint("api", __name__, url_prefix="/api/v1")


@api.route("/status", methods=["GET"])
def get_data():
    return render_template("api.html")
