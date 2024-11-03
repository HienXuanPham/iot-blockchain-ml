from flask import Flask
from threading import Thread
from paho.mqtt.client import Client

def on_message(client, userdata, message):
  print(f"Received message {message.payload.decode()} on topic {message.topic}")

def create_app():
  app = Flask(__name__)

  from iot_simulator import mqtt_simulator
  Thread(target=mqtt_simulator.main).start()

  mqtt_client = Client()
  mqtt_client.on_message = on_message
  mqtt_client.connect("localhost", 1883, 60)
  mqtt_client.subscribe("device/data")
  mqtt_client.loop_start()

  return app