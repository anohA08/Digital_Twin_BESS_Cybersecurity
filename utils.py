import os
import pandas as pd


def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    data = pd.read_csv(file_path)

    required_columns = ["Hour", "Solar", "Demand"]

    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing column: {column}")

    return data