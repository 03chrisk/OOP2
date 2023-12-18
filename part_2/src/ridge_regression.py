from src.regularized_regression import RegularizedRegression
import numpy as np


class RidgeRegression(RegularizedRegression):
    def _calculate_regularization_penalty(self) -> float:
        """
        Calculate the L2 regularization penalty for Ridge Regression.

        Returns:
            float: The L2 regularization penalty.
        """

        return self.lambda_ * np.sqrt(np.sum(np.square(self.coefficients)))

    def _calculate_gradient(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Calculate the gradient for Ridge Regression.

        Args:
            X (np.ndarray): The feature matrix.
            y (np.ndarray): The response vector.

        Returns:
            np.ndarray: The gradient of the loss function.
        """
        if not isinstance(X, np.ndarray) or not isinstance(y, np.ndarray):
            raise ValueError("Data must be an np.ndarray")

        predictions = X.dot(self.coefficients)
        residuals = y - predictions
        gradient = -2 * X.T.dot(residuals) / len(y)

        l2_penalty = 2 * self.coefficients * self.lambda_
        l2_penalty[0] = 0  # Excluding the bias term from regularization

        return gradient + l2_penalty
