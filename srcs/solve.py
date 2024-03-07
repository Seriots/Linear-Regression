from LinearComputedData import LinearComputedData
import pickle

def main():
    with open ('model.pkl', 'rb') as file:
        trainedModel = pickle.load(file)

        print(trainedModel.predict(int(input("Enter a value: "))))

if __name__ == '__main__':
    main()
