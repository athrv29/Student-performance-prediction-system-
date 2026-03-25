import numpy as np

def load_data():
    X = np.array([[1, 50, 40], [2, 55, 45], [3, 60, 50], [4, 65, 55], [5, 70, 60], [6, 75, 65], [7, 80, 70], [8, 85, 75], [9, 90, 80], [10, 95, 85]], dtype=float)
    y = np.array([42,48,52,57,63,68,72,78,85,90], dtype=float)
    return X, y

