from IMLearn.utils import split_train_test
from IMLearn.learners.regressors import LinearRegression

from typing import NoReturn, Optional
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "simple_white"


def preprocess_data(X: pd.DataFrame, y: Optional[pd.Series] = None):
    """
    preprocess data
    Parameters
    ----------
    X : DataFrame of shape (n_samples, n_features)
        Design matrix of regression problem

    y : array-like of shape (n_samples, )
        Response vector corresponding given samples

    Returns
    -------
    Post-processed design matrix and response vector (prices) - either as a single
    DataFrame or a Tuple[DataFrame, Series]
    """
    # X.drop(columns='id', axis=1, inplace=True)
    for column in X.loc[:, ~X.columns.isin(['date', 'lat', 'long'])]:
        X[column].replace(np.nan, X[column].mean())
    X.assign(lables=y)
    # X.drop((X.loc[:, ~X.columns.isin(['date', 'lat', 'long'])] < 0).all(1).index, inplace=True)
    X = X[(X.loc[:, ~X.columns.isin(['date', 'lat', 'long'])] >= 0).all(1)]
    # temp = X[(X.loc[:, ~X.columns.isin(['date', 'lat', 'long'])] >= 0).all(1)].merge(X.drop_duplicates(), on="id", how='left', indicator=True)
    # temp[temp['_merge'] == "both"]

    return X, y


def feature_evaluation(X: pd.DataFrame, y: pd.Series, output_path: str = ".") -> NoReturn:
    """
    Create scatter plot between each feature and the response.
        - Plot title specifies feature name
        - Plot title specifies Pearson Correlation between feature and response
        - Plot saved under given folder with file name including feature name
    Parameters
    ----------
    X : DataFrame of shape (n_samples, n_features)
        Design matrix of regression problem

    y : array-like of shape (n_samples, )
        Response vector to evaluate against

    output_path: str (default ".")
        Path to folder in which plots are saved
    """
    raise NotImplementedError()


if __name__ == '__main__':
    np.random.seed(0)
    df = pd.read_csv("../datasets/house_prices.csv")

    # Question 1 - split data into train and test sets
    train_X, train_y, test_X, test_y = split_train_test(df.drop('price', axis="columns"), df['price'])

    # Question 2 - Preprocessing of housing prices dataset
    preprocess_data(train_X, train_y)

    # Question 3 - Feature evaluation with respect to response
    # raise NotImplementedError()

    # Question 4 - Fit model over increasing percentages of the overall training data
    # For every percentage p in 10%, 11%, ..., 100%, repeat the following 10 times:
    #   1) Sample p% of the overall training data
    #   2) Fit linear model (including intercept) over sampled set
    #   3) Test fitted model over test set
    #   4) Store average and variance of loss over test set
    # Then plot average loss as function of training size with error ribbon of size (mean-2*std, mean+2*std)
    # raise NotImplementedError()
