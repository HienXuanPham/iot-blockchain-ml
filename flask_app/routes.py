from flask_app import data_from_devices
from flask import Blueprint, jsonify

app_bp = Blueprint("", __name__, url_prefix="/")

@app_bp.route("/", methods=["GET"])
def get_data():
  return jsonify(data_from_devices)