import pandas as pd
import numpy as np
import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split

# DATASET_PATH = '../CICIoT2023/'

# csv_files = [file for file in os.listdir(DATASET_PATH) if file.endswith('.csv')]

# csv_files.sort()

# dataset_df = pd.DataFrame()
# print("CSV files to be processed:", csv_files)

# for file in tqdm(csv_files):
#     file_path = os.path.join(DATASET_PATH, file)
#     df = pd.read_csv(file_path)
#     dataset_df = pd.concat([dataset_df, df], ignore_index=True)

# dataset_df.to_csv('dataset.csv', index=False)
# print("Dataset created and saved as dataset.csv")
# Output: 37349263 rows for train_data and 9337316 rows for test_data when using the full dataset
# Output: 3734926 and 933732 rows for train_data and test_data when using the 10% dataset
# output: 37349 and 9337 for train_data and test_data when using the 0.1% dataset

dataset = pd.read_csv('dataset.csv')
small_dataset = dataset.sample(frac=0.001, random_state=42)
train_data, test_data = train_test_split(small_dataset, test_size=0.2, random_state=42)
print(len(train_data), len(test_data)) 

train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)