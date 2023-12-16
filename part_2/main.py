# from src.multiple_linear_regression import MultipleLinearRegression
from src.lasso_regression import LassoRegression
from src.ridge_regression import RidgeRegression
from src.regression_plotter import RegressionPlotter

from sklearn import datasets
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

import numpy as np


def create_dataset(n: int) -> np.ndarray:
    X, y = datasets.make_regression(n_samples=5,
                                    n_features=n,
                                    noise=10,
                                    random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = create_dataset(2)

    alpha = 0.01  # Learning rate
    lambda_ = 0.01  # Regularization parameter
    iterations = 100  # Number of iterations
    max_iter = 100

    # Creating instances
    lasso_model = LassoRegression(alpha, lambda_, iterations, 'normal')
    ridge_model = RidgeRegression(alpha, lambda_, iterations, 'normal')

    lasso_sklearn = Lasso(alpha=alpha, max_iter=max_iter)
    ridge_sklearn = Ridge(alpha=alpha, max_iter=max_iter)

    lasso_model.train(X_train, y_train)
    ridge_model.train(X_train, y_train)

    lasso_sklearn.fit(X_train, y_train)
    ridge_sklearn.fit(X_train, y_train)

    lasso_predictions = lasso_model.predict(X_test)
    ridge_predictions = ridge_model.predict(X_test)

    lasso_predictions_sklearn = lasso_sklearn.predict(X_test)
    ridge_predictions_sklearn = ridge_sklearn.predict(X_test)

    print("Lasso:", lasso_predictions.flatten())
    print("Lasso SKLEARN:", lasso_predictions_sklearn)
    print("Ridge:", ridge_predictions.flatten())
    print("Ridge SKLEARN:", ridge_predictions_sklearn)

    mae_lasso = mean_absolute_error(y_test, lasso_predictions_sklearn)
    print(f"Lasso Regression MAE: {mae_lasso}")

    # Calculate MAE for Ridge
    mae_ridge = mean_absolute_error(y_test, ridge_predictions_sklearn)
    print(f"Ridge Regression MAE: {mae_ridge}")

    maee_lasso = mean_absolute_error(y_test, lasso_predictions)
    print(f"Lasso Regression MAE: {maee_lasso}")

    # Calculate MAE for Ridge
    maee_ridge = mean_absolute_error(y_test, ridge_predictions)
    print(f"Ridge Regression MAE: {maee_ridge}")

    print("my coefficients:", lasso_model.coefficients)
    print("SKLEARN")
    print("Coefficients:", lasso_sklearn.coef_)
    print("Intercept:", lasso_sklearn.intercept_)

    #plotterME = RegressionPlotter(ridge_model)
    #plotterSK = RegressionPlotter(ridge_sklearn)

    #plotterME.plot_model(X_test, y_test)
    #plotterSK.plot_model(X_test, y_test)
