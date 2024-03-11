# routes/api.py
from flask import Blueprint, jsonify, render_template
from datetime import datetime
from time import sleep

api = Blueprint("api", __name__, url_prefix="/api/v1")


@api.route("/status", methods=["GET"])
def get_data():
    return jsonify({"message": f"Tudo certo"}), 200


@api.route("/wait")
def wait():
    sleep(3)
    return "Waitado"
