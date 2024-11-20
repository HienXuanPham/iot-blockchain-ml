import paho.mqtt.client as mqtt
import pandas as pd
import time
from tqdm import tqdm

TEST_DATA_PATH = "data_preparation/test_data.csv"

X_columns = [
    'flow_duration', 'Header_Length', 'Protocol Type', 'Duration',
    'Rate', 'Srate', 'Drate', 'fin_flag_number', 'syn_flag_number',
    'rst_flag_number', 'psh_flag_number', 'ack_flag_number',
    'ece_flag_number', 'cwr_flag_number', 'ack_count',
    'syn_count', 'fin_count', 'urg_count', 'rst_count', 
    'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 'SSH', 'IRC', 'TCP',
    'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 'LLC', 'Tot sum', 'Min',
    'Max', 'AVG', 'Std', 'Tot size', 'IAT', 'Number', 'Magnitue',
    'Radius', 'Covariance', 'Variance', 'Weight', 
]

def simulate_data(client, topic):
  data_frame = pd.read_csv(TEST_DATA_PATH, usecols=X_columns)

  for _, row in tqdm(data_frame.iterrows()):
    message = row.tolist()
    client.publish(topic, str(message))
    time.sleep(0.05)

def main():
  client = mqtt.Client()
  client.connect("localhost", 1883, 60)
  client.loop_start()
  simulate_data(client, "device/data")
  client.loop_stop()
