from ArgsHandler import ArgsHandler, OptionObject, ArgsObject
from LinearRegression import LinearRegression
from DataLoader import DataLoader
import sys

def parse_user_input(user_input):
    DEFAULT_PATH = "data/test.csv"
    if len(sys.argv) < 2:
        print(f"Default path {DEFAULT_PATH} is used")
        return {"data_path": DEFAULT_PATH}
    print(f"User path {sys.argv[1]} is used")
    return {"data_path": sys.argv[1]}


def main():
    args_handler = ArgsHandler('This program perform a linear regression on a dataset', [
        ArgsObject('data_path', 'Path to the dataset.')
    ], [
        OptionObject('help', 'Show this help message.', name='h', expected_type=bool),
        OptionObject('learning_rate', 'Learning rate of the model.', name='l', expected_type=float),
        OptionObject('epochs', 'Number of epochs.', name='e', expected_type=int),
        OptionObject('output', 'The file to save the algorythm', name='o', expected_type=str),
    ], """""")

    try:
        user_input = args_handler.parse_args()
    except Exception as e:
        print(e)
        return
    if "help" in user_input:
        print(args_handler.full_help())
        return

    try:
        args_handler.check_args(user_input)
    except Exception as e:
        print(e)
        return
   
    data = DataLoader(user_input['args'][0])
   
    if data.data is None or data.by_column is None:
        return
    
    learning_rate = user_input["learning_rate"] if "learning_rate" in user_input else 0.07
    epochs = user_input["epochs"] if "epochs" in user_input else 1000
    output = user_input["output"] if "output" in user_input else "model.pkl"

    computedData = LinearRegression(data, learning_rate=learning_rate)

    computedData.generate_model(epochs=epochs)

    print(f"theta0(b) = {computedData.theta0}, theta1(m) = {computedData.theta1}, error = {computedData.error()}")

    computedData.save(output)

    computedData.display_data()


if __name__ == '__main__':
    main()