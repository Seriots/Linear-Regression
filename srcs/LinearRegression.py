import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from DataLoader import DataLoader


class LinearRegression:
    def __init__(self, data: DataLoader, learning_rate=0.001, theta0=0, theta1=0):
        """Initialize the LinearRegression with the given data."""
        self.data = data
        self.theta0 = theta0  # 8000
        self.theta1 = theta1  # -0.02
        self.learning_rate = learning_rate
        
        self.normalized_data = self.normalize_data()
        self.error_history = []

    def normalize_data(self):
        """Normalize the data. between 0 and 1"""
        x = self.data.by_column['x']
        y = self.data.by_column['y']
        meanx = self.data.by_column['x'].mean()
        stdx = self.data.by_column['x'].std()

        meany = self.data.by_column['y'].mean()
        stdy = self.data.by_column['y'].std()

        x = (x - meanx) / stdx
        y = (y - meany) / stdy
       
        return ({'x': x, 'y': y, 'theta0': 0, 'theta1': 0})

    def denormalize(self):
        """Denormalize the data."""
        meanx = self.data.by_column['x'].mean()
        stdx = self.data.by_column['x'].std()

        meany = self.data.by_column['y'].mean()
        stdy = self.data.by_column['y'].std() # ( ) **0.5

        self.theta0 = (stdy * self.normalized_data['theta0']) + meany - self.normalized_data['theta1'] * (stdy / stdx) * meanx
        self.theta1 = (stdy) * self.normalized_data['theta1'] / (stdx)

    def predict(self, data0):
        """Return the prediction of the model for the given data0."""
        return self.theta0 + self.theta1 * data0
    
    def predict_norm(self, data0):
        """Return the prediction of the model for the given data0 with normalized values."""
        return self.normalized_data['theta0'] + self.normalized_data['theta1'] * data0

    def error(self):
        """Return the cost of the model."""
        x = self.normalized_data['x']
        y = self.normalized_data['y']
        n = len(x)
        return (1 / 2*n) * sum([(self.predict_norm(x[i]) - y[i]) ** 2 for i in range(n)])

    def generate_model(self, epochs=1000):
        """Generate the model using the data from the DataLoader.
        This method should update the theta0 and theta1 attributes."""
        x, y = self.normalized_data['x'], self.normalized_data['y']
        n = len(x)

        for _ in range(epochs):
            D_m = self.learning_rate * (1 / n) * sum([x[i] * (self.predict_norm(x[i]) - y[i]) for i in range(n)])
            D_c = self.learning_rate * (1 / n) * sum([self.predict_norm(x[i]) - y[i] for i in range(n)])

            self.normalized_data['theta0'] -= D_c
            self.normalized_data['theta1'] -= D_m

            self.error_history.append((self.error()))

        self.denormalize()

    def display_data(self):
        """Display the data and the model in a plot"""
        fig = plt.figure(figsize=(8, 4))
        
        fig.add_subplot(1, 2, 1)

        sns.scatterplot(x=self.data.by_column['x'], y=self.data.by_column['y'])
        
        x = np.linspace(min(self.data.by_column['x']), max(self.data.by_column['x']))
        sns.lineplot(x=x, y=self.predict(x), color='red', legend='full', label='Prediction')
        plt.title('Data and prediction')
        plt.legend(loc='upper right')

        fig.add_subplot(1, 2, 2)
        sns.lineplot(x=range(len(self.error_history)), y=self.error_history, color='red', legend='full', label='Precision')
        plt.title('Precision')
        plt.legend(loc='upper right')
        plt.xlabel('Epochs')
        plt.ylabel('Precision')

        try:
            plt.show()
        except KeyboardInterrupt:
            print("Interrupted by user")

    def save(self, filename):
        """Save the model to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
