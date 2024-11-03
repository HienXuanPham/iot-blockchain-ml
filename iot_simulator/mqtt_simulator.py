import paho.mqtt.client as mqtt
import random
import time

def simulate_normal_data(client, topic):
  for i in range(30):
    client.publish(topic, f"{i}: normal data")
    time.sleep(random.uniform(0.7, 2.1))
  
def simulate_anomaly_data(client, topic):
  for i in range(70):
    client.publish(topic, f"{i}: anomaly data")
    time.sleep(random.uniform(0.01, 0.09))

def main():
  client = mqtt.Client()
  client.connect("localhost", 1883, 60)
  client.loop_start()
  simulate_normal_data(client, "device/data")
  simulate_anomaly_data(client, "device/data")
