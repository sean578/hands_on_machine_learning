import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit


def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)


def split_into_training_test_datasets(data_frame, feature_to_use, bins, test_fraction, random_seed):

    # Create a new categorical variable for income
    data_frame['income_cat'] = pd.cut(data_frame[feature_to_use],
                                      bins=bins,
                                      labels=[x + 1 for x in range(len(bins)-1)])

    # Use sk-learns function to split up the dataset based on these new categories
    split = StratifiedShuffleSplit(n_splits=1, test_size=test_fraction, random_state=random_seed)

    for train_index, test_index in split.split(data_frame, data_frame['income_cat']):
        strat_train_set = data_frame.loc[train_index]  # how does this appending work?
        strat_test_set = data_frame.loc[test_index]

    # Clean new datasets by removing the income cateorical variable
    for set_ in (strat_train_set, strat_test_set):
        set_.drop('income_cat', axis=1, inplace=True)

    return strat_train_set, strat_test_set

if __name__ == '__main__':

    HOUSING_PATH = os.path.join("datasets", "housing")

    # Create a dataframe from the csv file
    housing = load_housing_data(HOUSING_PATH)

    # Split the dataframe into train/test datasets
    feature_for_splitting = 'median_income'
    bin_edges = [0., 1.5, 3.0, 4.5, 6., np.inf]
    test_fraction_of_dataset = 0.2
    seed = 42

    train_set, test_set = split_into_training_test_datasets(housing, feature_for_splitting, bin_edges, test_fraction_of_dataset, seed)
    print(train_set.info())
    print(test_set.info())
