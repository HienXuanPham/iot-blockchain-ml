from flask_app import data_from_devices
from flask import Blueprint, jsonify
from machine_learning.anomaly_detector import detector

app_bp = Blueprint("h", __name__, url_prefix="/h")

@app_bp.route("/", methods=["GET"])
def get_data():
  return jsonify(data_from_devices)

@app_bp.route("/detect", methods=["GET"])
def detect_anomalies():
  if data_from_devices:
    prediction = detector.predict(data_from_devices)

    return jsonify(prediction.tolist())
  else:
    return jsonify("Something went wrong"), 400