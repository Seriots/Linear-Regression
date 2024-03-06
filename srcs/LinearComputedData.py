import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from DataLoader import DataLoader


class LinearComputedData():
    def __init__(self, data: DataLoader):
        """Initialize the LinearComputedData with the given data."""
        self.data = data
        self.theta0 = 0  # 8000
        self.theta1 = 0  # -0.02
        self.learning_rate = 0.0001

    def predict(self, data0):
        """Return the prediction of the model for the given data0."""
        return self.theta0 + self.theta1 * data0

    def error(self):
        """Return the cost of the model."""
        x = self.data.by_column[0]
        y = self.data.by_column[1]
        n = len(x)
        return (1 / (n)) * sum([(y[i] - self.predict(x[i])) ** 2 for i in range(n)])

    def generate_model(self):
        """Generate the model using the data from the DataLoader.
        This method should update the theta0 and theta1 attributes."""
        
        

    def save(self, filename):
        """Save the model to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    def display_data(self):
        """Display the data and the model in a plot"""
        sns.scatterplot(x=self.data.by_column[0], y=self.data.by_column[1])
        
        x = np.linspace(min(self.data.by_column[0]), max(self.data.by_column[0]))
        sns.lineplot(x=x, y=self.predict(x), color='red', legend='full', label='Prediction')
        
        plt.legend(loc='upper right')
        try:
            plt.show()
        except KeyboardInterrupt:
            print("Interrupted by user")
