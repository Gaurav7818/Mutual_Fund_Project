import pandas as pd
import os

folder = "../data/raw"

files = os.listdir(folder)

for file in files:

    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("="*50)
        print("File:", file)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())