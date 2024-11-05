from flask_app import data_from_devices
from flask import Blueprint, jsonify
from machine_learning.anomaly_detector import anomaly_detector
import numpy

app_bp = Blueprint("h", __name__, url_prefix="/h")

@app_bp.route("/", methods=["GET"])
def get_data():
  return jsonify(data_from_devices)

@app_bp.route("/detect", methods=["GET"])
def detect_anomalies():
  predictions = anomaly_detector(data_from_devices)
  print(f"Predictions: {predictions}")
  return jsonify(predictions.tolist())