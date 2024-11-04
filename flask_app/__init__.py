from flask import Flask
from threading import Thread
from paho.mqtt.client import Client

data_from_devices = []

def on_message(client, userdata, message):
  data_from_devices.append(int(message.payload.decode()))
  print(f"Received message: {message.payload.decode()}")

def create_app():
  app = Flask(__name__)

  from iot_simulator import mqtt_simulator
  Thread(target=mqtt_simulator.main).start()

  mqtt_client = Client()
  mqtt_client.on_message = on_message
  mqtt_client.connect("localhost", 1883, 60)
  mqtt_client.subscribe("device/data")
  mqtt_client.loop_start()

  from flask_app.routes import app_bp
  app.register_blueprint(app_bp)

  return app