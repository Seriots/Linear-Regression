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
        self.theta0 = theta0  # 8000
        self.theta1 = theta1  # -0.02
        self.learning_rate = learning_rate
        self.normalized_data= None

    def normalize_data(self):
        """Normalize the data. between 0 and 1"""
        x = self.data.by_column[0]
        y = self.data.by_column[1]

        x = (x - min(x)) / (max(x) - min(x))
        y = (y - min(y)) / (max(y) - min(y))
       
        return (x, y)

    def predict(self, data0):
        """Return the prediction of the model for the given data0."""
        return self.theta0 + self.theta1 * data0
    
    def predict_norm(self, data0):
        """Return the prediction of the model for the given data0."""
        return self.normalized_data[0] + self.normalized_data[1] * data0

    def error(self):
        """Return the cost of the model."""
        x = self.data.by_column[0]
        y = self.data.by_column[1]
        n = len(x)
        return (1 / 2*n) * sum([(self.predict(x[i]) - y[i]) ** 2 for i in range(n)])


    def generate_model(self, epochs=1000):
        """Generate the model using the data from the DataLoader.
        This method should update the theta0 and theta1 attributes."""
        x, y = self.normalize_data()
        n = len(x)

        for _ in range(epochs):
            D_m = self.learning_rate * (1 / n) * sum([x[i] * (self.predict(x[i]) - y[i]) for i in range(n)])
            D_c = self.learning_rate * (1 / n) * sum([self.predict(x[i]) - y[i] for i in range(n)])

            self.theta0 -= D_c
            self.theta1 -= D_m

        self.normalized_data = (self.theta0, self.theta1, x, y)

        deltax = max(self.data.by_column[0]) - min(self.data.by_column[0])
        deltay = max(self.data.by_column[1]) - min(self.data.by_column[1])

        tmp0 = self.theta0
        tmp1 = self.theta1

        self.theta0 = (deltay * tmp0) + min(self.data.by_column[1]) - tmp1 * (deltay / deltax) * min(self.data.by_column[0])
        self.theta1 = (deltay) * tmp1 / (deltax)
        
    def display_data(self):
        """Display the data and the model in a plot"""
        fig = plt.figure(figsize=(10, 5))
        
        fig.add_subplot(1, 2, 1)

        sns.scatterplot(x=self.data.by_column[0], y=self.data.by_column[1])
        
        x = np.linspace(min(self.data.by_column[0]), max(self.data.by_column[0]))
        sns.lineplot(x=x, y=self.predict(x), color='red', legend='full', label='Prediction')
        
        plt.legend(loc='upper right')

        fig.add_subplot(1, 2, 2)
        sns.scatterplot(x=self.normalized_data[2], y=self.normalized_data[3])
        
        x2 = np.linspace(min(self.normalized_data[2]), max(self.normalized_data[2]))
        sns.lineplot(x=x2, y=self.predict_norm(x2), color='red', legend='full', label='Prediction')
        
        plt.legend(loc='upper right')
        try:
            plt.show()
        except KeyboardInterrupt:
            print("Interrupted by user")

    def save(self, filename):
        """Save the model to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
