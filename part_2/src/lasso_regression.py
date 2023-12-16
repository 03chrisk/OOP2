import numpy as np
from src.regularized_regression import RegularizedRegression


class LassoRegression(RegularizedRegression):
    def _calculate_regularization_penalty(self):
        return self.lambda_ * np.sum(np.abs(self.coefficients))

    def _calculate_gradient(self, X, y):
        predictions = X.dot(self.coefficients)
        residuals = y - predictions
        gradient = -2 * X.T.dot(residuals) / len(y)

        l1_penalty = self.lambda_ * np.sign(self.coefficients)
        l1_penalty[0] = 0  # Excluding the bias term from regularization

        return gradient + l1_penalty
