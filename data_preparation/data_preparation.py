import pandas as pd
import numpy as np
import os
from tqdm import tqdm

DATASET_PATH = '../CICIoT2023/'

csv_files = [file for file in os.listdir(DATASET_PATH) if file.endswith('.csv')]

csv_files.sort()

dataset_df = pd.DataFrame()
print("CSV files to be processed:", csv_files)

for file in tqdm(csv_files):
    file_path = os.path.join(DATASET_PATH, file)
    df = pd.read_csv(file_path)
    dataset_df = pd.concat([dataset_df, df], ignore_index=True)

dataset_df.to_csv('dataset.csv', index=False)
print("Dataset created and saved as dataset.csv")