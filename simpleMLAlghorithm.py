import numpy as np

def main():
    # Buat training data
    x_train = np.array([1,2,3,4,5])
    y_train = np.array([1,4,9,16,25])

    # buat model
    model = np.polyfit(x_train,y_train,2)
    
    # Make prediction
    x_test = int(input('input x: '))
    y_pred = np.polyval(model,x_test)

    # print the prediction
    print(y_pred)

if __name__ == "__main__":
    main()

   