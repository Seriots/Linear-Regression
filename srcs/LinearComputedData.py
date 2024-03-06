import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from DataLoader import DataLoader


class LinearComputedData():
    def __init__(self, data: DataLoader, learning_rate=0.001, theta0=0, theta1=0):
        """Initialize the LinearComputedData with the given data."""
        self.data = data
        self.normalized_data = self.normalize_data()
        self.theta0 = 8000  # 8000
        self.theta1 = theta1  # -0.02
        self.learning_rate = learning_rate

    def normalize_data(self):
        """Normalize the data. between 0 and 1"""
        x = self.data.by_column[0]
        y = self.data.by_column[1]
        x = (x - min(x)) / (max(x) - min(x))
        y = (y - min(y)) / (max(y) - min(y))
       
        print(f"Normalized data: {x}, {y}")
        return (x, y)

    def predict(self, data0):
        """Return the prediction of the model for the given data0."""
        return self.theta0 + self.theta1 * data0

    def error(self):
        """Return the cost of the model."""
        x = self.normalized_data[0]
        y = self.normalized_data[1]
        n = len(x)
        return (1 / (n)) * sum([(y[i] - self.predict(x[i])) ** 2 for i in range(n)])


    def generate_model(self, epochs=1000):
        """Generate the model using the data from the DataLoader.
        This method should update the theta0 and theta1 attributes."""
        x = self.normalized_data[0]
        y = self.normalized_data[1]
        n = len(x)

        print(f"Initial error: {self.error()}")
        for _ in range(epochs):
            D_m = self.learning_rate * (1 / (n)) * sum([x[i] * (self.predict(x[i]) - y[i]) for i in range(n)])
            D_c = self.learning_rate * (1 / (n)) * sum([self.predict(x[i]) - y[i] for i in range(n)])

            self.theta0 = self.theta0 - D_c
            self.theta1 = self.theta1 - D_m
        
            #print(f"Final error: {self.error()}")


    def save(self, filename):
        """Save the model to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    def aled(self):
        """Display the data and the model in a plot"""
        sns.scatterplot(x=self.data.by_column[0], y=self.data.by_column[1])
        
        x = np.linspace(min(self.data.by_column[0]), max(self.data.by_column[0]))
        sns.lineplot(x=x, y=self.predict(x), color='red', legend='full', label='Prediction')
        
        plt.legend(loc='upper right')
        try:
            plt.show()
        except KeyboardInterrupt:
            print("Interrupted by user")


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
