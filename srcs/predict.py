from ArgsHandler import ArgsHandler, OptionObject
import pickle


def main():
    args_handler = ArgsHandler('This program perform a linear regression on a dataset', [
    ], [
        OptionObject('help', 'Show this help message.', name='h', expected_type=bool),
        OptionObject('model_path', 'Path to the model.', name='m', expected_type=str),
        OptionObject('mileage', 'Mileage of the car.', name='i', expected_type=int),
    ], """""")

    try:
        user_input = args_handler.parse_args()
    except Exception as e:
        print(e)
        return
    if "help" in user_input:
        print(args_handler.full_help())
        return

    model = user_input["model_path"] if "model_path" in user_input else "model.pkl"
    mileage = user_input["mileage"] if "mileage" in user_input else None

    try:
        with open(model, 'rb') as file:
            trainedModel = pickle.load(file)
            
            if mileage is None:
                mileage = int(input("Enter a value: "))

            print(trainedModel.predict(mileage))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
