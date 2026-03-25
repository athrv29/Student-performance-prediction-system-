import numpy as np

def train_model(X,y):
    ones = np.ones((X.shape[0], 1))
    X = np.hstack((ones, X))
    parameter = np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(y)
    assumed_y = X.dot(parameter)
    err= np.mean(np.abs(assumed_y - y))
    return parameter, assumed_y, err

def predict_student(parameter, h, attend, previous_marks):
    new_data = np.array([[1, h, attend, previous_marks]])
    prediction = new_data.dot(parameter)
    return prediction