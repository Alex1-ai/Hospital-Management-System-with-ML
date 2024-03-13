import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import os
import pickle






def predict_diabetes(input_data):
    # loading the diabetes dataset
    file_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'diabetes.csv')
    diabetes_dataset = pd.read_csv(file_path)
    # print(diabetes_dataset.head())

    X = diabetes_dataset.drop(columns="Outcome", axis=1)
    # print(X)

    scaler = StandardScaler()
    scaler.fit(X)
    file_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'diabetes_trained_model.sav')
    loaded_model = pickle.load(open(file_path, 'rb'))
    # changing  the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardized the input data
    std_data = scaler.transform(input_data_reshaped)
    # print(std_data)

    prediction = loaded_model.predict(std_data)
    # print(prediction)

    if (prediction[0] == 0):
    #    print("The person does not have a Heart Disease")
       return "The result shows this patient is negative"
    else:
    #    print("The Person has Heart Disease")
       return "The result shows this patient is positive"
    
# predict_diabetes([4, 110, 92, 0, 0, 37.6, 0.191, 30])


def predict_heart_disease(input_data):
   # loading models for heart disease 
    file_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'heart_disease_trained_model.sav')
    loaded_model = pickle.load(open(file_path, 'rb'))
    # change the input data to a numpy array
    input_data_as_numpy_array = np.array(input_data)

        # reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
        
    if (prediction[0] == 0):
        # print("The person does not have a Heart Disease")
        return "The result shows this patient is negative"
            # return render(request, 'heartdisease.html', {"context":context})    
    else:
        # print("The Person has Heart Disease")
        return "The result shows this patient is positive"
    
# predict_heart_disease((62,0,0, 140,268,0,0,160,0,3.6,0,2,2))