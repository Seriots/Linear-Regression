from LinearComputedData import LinearComputedData
from DataLoader import DataLoader
import sys

def parse_user_input() -> dict:
    DEFAULT_PATH = "data/test.csv"
    if len(sys.argv) < 2:
        print(f"Default path {DEFAULT_PATH} is used")
        return {"data_path": DEFAULT_PATH}
    print(f"User path {sys.argv[1]} is used")
    return {"data_path": sys.argv[1]}


def main():
    user_input: dict = parse_user_input()
   
    data = DataLoader(user_input["data_path"])
   
    if data.data is None or data.by_column is None:
        return
    
    computedData = LinearComputedData(data, learning_rate=0.07, theta0=0, theta1=0)

    computedData.generate_model(epochs=1000)
    print(f"Error before: {computedData.error()}")

    print(f"theta0(b) = {computedData.theta0}, theta1(m) = {computedData.theta1}, error = {computedData.error()}")

    computedData.save("model.pkl")

    computedData.display_data()


if __name__ == '__main__':
    main()