from src.lasso_regression import LassoRegression
from src.ridge_regression import RidgeRegression
from src.regression_plotter import RegressionPlotter
from src.model_saver import ModelSaver
from src.generic_ml_model import MachineLearningModel
import numpy as np


def test_model_saver(model: MachineLearningModel,
                     format: str) -> None:
    print("Coefficients of the model we are saving: ")
    print(model.coefficients)

    saver = ModelSaver()
    saver.save_model(model, format_type=format, filename='saved_model')

    coefficients = saver.load_model(format_type=format, filename='saved_model')
    model2 = RidgeRegression(0.01, 0.01, 1000, 'normal')
    model2.coefficients = coefficients
    print("Coefficients of the loaded model: ")
    print(model2.coefficients)


if __name__ == "__main__":
    data = np.load('dataset.npz')
    X_train = data['X_train']
    X_test = data['X_test']
    y_train = data['y_train']
    y_test = data['y_test']

    alpha = 0.01  # Learning rate
    lambda_ = 0.01  # Regularization parameter
    iterations = 1000  # Number of iterations
    max_iter = 1000

    # Creating instances
    lasso_model = LassoRegression(alpha, lambda_, iterations, 'normal')
    ridge_model = RidgeRegression(alpha, lambda_, iterations, 'normal')

    lasso_model.train(X_train, y_train)
    ridge_model.train(X_train, y_train)

    lasso_predictions = lasso_model.predict(X_test)
    ridge_predictions = ridge_model.predict(X_test)

    print("Ridge model intercept:", ridge_model.coefficients[0])
    print("Ridge model weights:", ridge_model.coefficients[1:])

    print("Lasso model intercept:", lasso_model.coefficients[0])
    print("Lasso model weights:", lasso_model.coefficients[1:])

    plotterME = RegressionPlotter(ridge_model)
    plotterME.plot_model(X_test, y_test)

    print("SAVER TEST .json")
    test_model_saver(ridge_model, format='json')
