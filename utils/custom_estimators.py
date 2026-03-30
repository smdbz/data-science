import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class DropMissingColumns(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # Find columns that do NOT have any NaNs during training
        # np.isnan(X).any(axis=0) checks each column for NaNs
        # The ~ symbol inverts it, keeping only the "clean" columns
        self.valid_cols_ = ~np.isnan(X).any(axis=0)
        return self

    def transform(self, X):
        # Apply that exact same column mask to any new data
        return X[:, self.valid_cols_]
