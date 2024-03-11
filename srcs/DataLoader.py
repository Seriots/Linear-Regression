import pandas

from ArgCheckDecorator import checkCSV


class DataLoader:
    def __init__(self, data_path):
        self.data = None;
        self.by_column = None
        self.load_data(data_path)

    @checkCSV
    def load_data(self, data_path):
        try:
            self.data = pandas.read_csv(data_path)
            self.by_column = {'x': self.data[self.data.columns[0]], 'y': self.data[self.data.columns[1]]}
        except Exception as e:
            print(f"Error: {e}")
