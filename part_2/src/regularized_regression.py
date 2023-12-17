import numpy as np
from abc import ABC, abstractmethod
from src.multiple_linear_regression import MultipleLinearRegression
import logging
from sklearn.metrics import mean_absolute_error

# Configure logging
logging.basicConfig(filename='training.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


class RegularizedRegression(MultipleLinearRegression, ABC):
    def __init__(self, alpha, lambda_, m, init_strat):
        super().__init__()
        self.alpha = alpha  # Learning rate
        self.lambda_ = lambda_  # Regularization parameter
        self.m = m  # Number of iterations
        self.init_strat = init_strat

    def _initialize_coefficients(self, n_features):
        if self.init_strat == 'uniform':
            return np.random.uniform(-1, 1, n_features + 1)
        elif self.init_strat == 'normal':
            return np.random.normal(0, 1, n_features + 1)
        else:
            raise ValueError("Unknown initialization strategy")

    def train(self, X_train, y_train):
        n_samples, n_features = X_train.shape
        self.coefficients = self._initialize_coefficients(n_features)

        X_b = np.c_[np.ones(len(X_train)), X_train]  # Add bias term

        for iteration in range(self.m):
            predictions = self.predict(X_train)
            residuals = y_train - predictions
            loss = self._calculate_loss(residuals)
            mae = np.average(np.abs(residuals))
            logging.info(
                f'Iteration {iteration+1}/{self.m}, Loss: {loss}, MAE: {mae}')

            gradients = self._calculate_gradient(X_b, y_train)
            self.coefficients -= self.alpha * gradients

    def _calculate_loss(self, residuals):
        mse = np.mean(residuals ** 2)
        regularization_penalty = self._calculate_regularization_penalty()
        return mse + regularization_penalty

    def _calculate_regularization_penalty(self):
        # This method is implemented in LassoRegression and RidgeRegression
        pass

    @abstractmethod
    def _calculate_gradient(self, X, y):
        pass
