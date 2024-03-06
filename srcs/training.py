from LinearComputedData import LinearComputedData
from DataLoader import DataLoader
import sys

def parse_user_input() -> dict:
    DEFAULT_PATH = "data/data.csv"
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
    
    computedData = LinearComputedData(data)

    computedData.generate_model()

    print(f"theta0 = {computedData.theta0}, theta1 = {computedData.theta1}")

    computedData.save("model.pkl")

    computedData.display_data()


if __name__ == '__main__':
    main()