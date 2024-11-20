import time
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy
import pandas as pd

TRAIN_DATA_PATH = "data_preparation/train_data.csv"

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
y_column = 'label'

class Detector:
  def __init__(self):
    self.scaler = StandardScaler()
    self.model = IsolationForest(contamination='auto')

  def train_machine(self):
    data_frame = pd.read_csv(TRAIN_DATA_PATH, usecols=X_columns)
    training_data = self.scaler.fit_transform(data_frame[X_columns])
    start_time = time.time()
    self.model.fit(training_data)
    end_time = time.time()

    print(f"Training time: {end_time - start_time}")

  def predict(self, data):
    lists_data = [eval(item) for item in data]
    IoT_data = pd.DataFrame(lists_data, columns=X_columns)
    transform_data = self.scaler.transform(IoT_data)
    predictions = self.model.predict(transform_data)

    return predictions

detector = Detector()
detector.train_machine()
