import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class FeatureSelectorTransformer(BaseEstimator, TransformerMixin):
    """ Delete columns of features set to False in columns_to_use
    """

    def __init__(self, columns_to_use, pandas):
        self.columns_to_use = columns_to_use
        self.pandas = pandas

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        if self.pandas:
            return X.iloc[:, self.columns_to_use]
        else:
            return X[:, self.columns_to_use]


if __name__ == '__main__':

    cols = [True, False, True, False, True, True, False, True]

    # An example with pandas dataframe...

    TRAINING_DATA_SAVE = './data/training_data'
    df = pd.read_pickle(TRAINING_DATA_SAVE)

    transformer_pandas = FeatureSelectorTransformer(cols, pandas=True)
    transformed_array = transformer_pandas.transform(df)

    # An example with a numpy array...

    an_example_array = np.random.rand(10, 8)

    transformer_numpy = FeatureSelectorTransformer(cols, pandas=False)
    transformed_array = transformer_numpy.transform(an_example_array)