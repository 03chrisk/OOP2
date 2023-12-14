from abc import ABC, abstractmethod


class MachineLearningModel(ABC):
    @abstractmethod
    def train(self, X_train, y_train):
        """
        Train the machine learning model with training data.

        Args:
            X_train: Training data features.
            y_train: Training data labels.
        """
        pass

    @abstractmethod
    def predict(self, X_test):
        """
        Predict using the machine learning model.

        Args:
            X_test: Data for making predictions.
        """
        pass

    @abstractmethod
    def get_coefficients(self):
        """
        Get the model's coefficients.
        """
        pass
