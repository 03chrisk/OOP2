import numpy as np
from src.regularized_regression import RegularizedRegression


class LassoRegression(RegularizedRegression):
    def _calculate_regularization_penalty(self) -> float:
        """
        Calculate the L1 regularization penalty for Lasso Regression.

        Returns:
            float: The L1 regularization penalty.
        """

        return self.lambda_ * np.sum(np.abs(self.coefficients))

    def _calculate_gradient(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Calculate the gradient for Lasso Regression.

        Args:
            X (np.ndarray): The feature matrix.
            y (np.ndarray): The response vector.

        Returns:
            np.ndarray: The gradient of the loss function.
        """

        predictions = X.dot(self.coefficients)
        residuals = y - predictions
        gradient = -2 * X.T.dot(residuals) / len(y)

        l1_penalty = self.lambda_ * np.sign(self.coefficients)
        l1_penalty[0] = 0  # Excluding the bias term from regularization

        return gradient + l1_penalty
