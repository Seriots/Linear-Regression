from LinearComputedData import LinearComputedData
import pickle

def main():
    with open ('model.pkl', 'rb') as file:
        trainedModel = pickle.load(file)

        print(trainedModel.predict(20))

if __name__ == '__main__':
    main()
