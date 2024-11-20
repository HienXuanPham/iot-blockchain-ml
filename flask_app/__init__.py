from flask import Flask
from threading import Thread
from paho.mqtt.client import Client
from machine_learning.anomaly_detector import detector


data_from_devices = []

def on_message(client, userdata, message):
  global data_from_devices
  data_from_iot_devices = message.payload.decode()
  data_from_devices.append(data_from_iot_devices)
  # print(f"Received message: {data_from_iot_devices}")

def create_app():
  app = Flask(__name__)

  from iot_simulator import mqtt_simulator
  Thread(target=mqtt_simulator.main).start()

  # if data_from_devices:
  #   detector.train_machine(data_from_devices)

  mqtt_client = Client()
  mqtt_client.on_message = on_message
  mqtt_client.connect("localhost", 1883, 60)
  mqtt_client.subscribe("device/data")
  mqtt_client.loop_start()

  from flask_app.routes import app_bp
  app.register_blueprint(app_bp)

  return app