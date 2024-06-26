import numpy as np
from abc import ABC, abstractmethod
from src.multiple_linear_regression import MultipleLinearRegression
import logging

# Configure logging
logging.basicConfig(filename='training.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


class RegularizedRegression(MultipleLinearRegression, ABC):
    def __init__(self, alpha: float, lambda_: float,
                 num_iter: int, init_strat: str) -> None:
        """
        Initialize the Regularized Regression model.

        Args:
            alpha (float): Learning rate.
            lambda_ (float): Regularization parameter.
            m (int): Number of iterations.
            init_strat (str): Initialization strategy, either 'uniform' or
            'normal'.
        """
        super().__init__()
        self._alpha = alpha
        self._lambda_ = lambda_
        self._num_iter = num_iter
        self._init_strat = init_strat

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if value <= 0:
            raise ValueError("Alpha must be positive")
        self._alpha = value

    @property
    def lambda_(self):
        return self._lambda_

    @lambda_.setter
    def lambda_(self, value):
        if value < 0:
            raise ValueError("Lambda must be non-negative")
        self._lambda_ = value

    @property
    def num_iter(self):
        return self._num_iter

    @num_iter.setter
    def m(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Number of iterations must be a positive integer")
        self._num_iter = value

    @property
    def init_strat(self):
        return self._init_strat

    @init_strat.setter
    def init_strat(self, value):
        if value not in ['uniform', 'normal']:
            raise ValueError(
                "Initialization strategy must be 'uniform' or 'normal'")
        self._init_strat = value

    def _initialize_coefficients(self, n_features: int) -> np.ndarray:
        if self.init_strat == 'uniform':
            return np.random.uniform(-1, 1, n_features + 1)
        elif self.init_strat == 'normal':
            return np.random.normal(0, 1, n_features + 1)
        else:
            raise ValueError("Unknown initialization strategy")

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        '''
        Trains the model using the provided training data. This method updates
        the model's coefficients based on gradient descent optimization.

        Args:
            X_train (numpy.ndarray): The independent variables (features) of
            the training data.
            y_train (numpy.ndarray): The dependent variable (target) of the
            training data.

        Returns:
            None

        Raises:
            ValueError: If either X_train or y_train is not an instance of
            numpy.ndarray.
        '''

        if not isinstance(X_train, np.ndarray) or not isinstance(y_train,
                                                                 np.ndarray):
            raise ValueError("Training data must be an np.ndarray")

        n_features = X_train.shape[1]
        self.coefficients = self._initialize_coefficients(n_features)

        X_b = np.c_[np.ones(len(X_train)), X_train]  # Add bias term

        for iteration in range(self.num_iter):
            predictions = self.predict(X_train).flatten()
            residuals = y_train - predictions
            loss = self._calculate_loss(residuals)
            mae = self._calculate_mae(residuals)
            logging.info(
                f'Iteration {iteration+1}/{self.num_iter},\
                      Loss: {loss}, MAE: {mae}')

            gradients = self._calculate_gradient(X_b, y_train)
            self.coefficients -= self.alpha * gradients

    def _calculate_loss(self, residuals: np.ndarray) -> float:
        '''
        Calculates the loss for the current model predictions using Mean
        Squared Error (MSE) and adds a regularization penalty.

        Args:
            residuals (numpy.ndarray): The difference between the actual values
            and the predicted values from the model.

        Returns:
            float: The calculated loss value, which is the sum of MSE and the
            regularization penalty.

        Raises:
            ValueError: If residuals is not an instance of numpy.ndarray.
        '''

        if not isinstance(residuals, np.ndarray):
            raise ValueError("Training data must be an np.ndarray")

        mse = np.mean(residuals ** 2)
        regularization_penalty = self._calculate_regularization_penalty()

        return mse + regularization_penalty

    def _calculate_mae(self, residuals: np.ndarray) -> float:
        '''
        Calculates the Mean Absolute Error (MAE) of the model's predictions.

        Args:
            residuals (numpy.ndarray): The difference between the actual values
            and the predicted values from the model.

        Returns:
            float: The calculated mean absolute error.

        Raises:
            ValueError: If residuals is not an instance of numpy.ndarray.
        '''
        if not isinstance(residuals, np.ndarray):
            raise ValueError("Training data must be an np.ndarray")

        return np.mean(np.abs(residuals))

    @abstractmethod
    def _calculate_regularization_penalty(self) -> float:
        """
        Abstract method to calculate the regularization penalty.

        Returns:
            float: The regularization penalty.
        """
        pass

    @abstractmethod
    def _calculate_gradient(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Abstract method to calculate the gradient of the loss function.

        Args:
            X (np.ndarray): The feature matrix.
            y (np.ndarray): The response vector.

        Returns:
            np.ndarray: The gradient of the loss function.
        """
        pass
