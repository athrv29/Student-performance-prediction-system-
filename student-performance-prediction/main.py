from data import load_data
from model import train_model, predict_student

X, y = load_data()
parameter, assumed_y, error = train_model(X, y)
print("Learned parameters:", parameter)
print(" Model is Trained Successfully!")
print(f"Error in training model (MAE): {error:.2f}")

print("Model Parameters:")
print("Complete parameter vectors:", parameter)
print("Bias w0:", parameter[0])
print("Weight for how many hours studied w1:", parameter[1])
print("Weight for how much is your attendance w2:", parameter[2])
print("Weight for marks w3:", parameter[3])

print("Enter the details of the students")
h = float(input("How many hours studied: "))
attend = float(input("how much is your attendence (%): ")) 
marks = float(input("Enter your marks: "))

result = predict_student(parameter, h, attend, marks)
print("predicted student final marks:", result)
