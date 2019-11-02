import pandas as pd
import os


def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)


if __name__ == '__main__':

    HOUSING_PATH = os.path.join("datasets", "housing")

    housing = load_housing_data(HOUSING_PATH)
    print(housing.head())
