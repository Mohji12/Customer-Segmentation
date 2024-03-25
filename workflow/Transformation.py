from sklearn.base import BaseEstimator, TransformerMixin


class DateTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()

        X_copy['Day_of_Joining'] = X_copy['Dt_Customer'].dt.day
        X_copy['Month_of_Joining'] = X_copy['Dt_Customer'].dt.month
        X_copy['Year_of_Joining'] = X_copy['Dt_Customer'].dt.year
        X_copy.drop(['Dt_Customer'], axis=1, inplace=True)

        return X_copy