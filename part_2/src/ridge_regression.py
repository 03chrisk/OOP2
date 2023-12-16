from src.regularized_regression import RegularizedRegression
import numpy as np


class RidgeRegression(RegularizedRegression):
    def _calculate_regularization_penalty(self):
        return self.lambda_ * np.sum(np.square(self.coefficients))

    def _calculate_gradient(self, X, y):
        predictions = X.dot(self.coefficients)
        residuals = y - predictions
        gradient = -2 * X.T.dot(residuals) / len(y)

        l2_penalty = 2 * self.coefficients * self.lambda_
        l2_penalty[0] = 0  # Excluding the bias term from regularization

        return gradient + l2_penalty
