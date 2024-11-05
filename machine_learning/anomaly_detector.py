from sklearn.ensemble import IsolationForest
import numpy

def anomaly_detector(data):
  converted_data = numpy.array(data).reshape(-1, 1)
  model = IsolationForest(contamination=0.5)
  model.fit(converted_data)
  predictions = model.predict(converted_data)

  return predictions
