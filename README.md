# 🎓 Student Performance Prediction System

> A machine learning project that predicts student academic performance using **Linear Regression**.

---

## 📌 Overview

The **Student Performance Prediction System** uses Linear Regression to analyze student data — such as study hours, attendance, and previous grades — to predict final exam scores. This helps educators identify at-risk students early and take timely action.

---

## 📂 Project Structure

```
student-performance-prediction/
│
├── main.py          # Trains the machine learning model
├── model.py         # Defines and evaluates prediction model
├── data.py          # Loads and preprocesses student data
├── _pycache_        # Stores compiled python file
├── report           # Contains project reports and outputs
└── README.md        # Project documentation
```

---

## 🧠 Model

**Algorithm:** Linear Regression (Ordinary Least Squares)

```
ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```

- `ŷ` = Predicted student score  
- `β₀` = Intercept  
- `β₁...βₙ` = Feature coefficients  
- `x₁...xₙ` = Input features (study hours, attendance, etc.)

---

## 📊 Dataset Features

| Feature | Description |
|---|---|
| `study_hours` | Daily average study hours |
| `attendance_rate` | Class attendance percentage |
| `previous_score` | Score from previous semester |
| **`final_score`** | **Target — final exam score** |

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Usage

### Train the Model

```bash
python model.py
```

Loads the dataset, trains the Linear Regression model, and saves it as `model.pkl`.

### Test the Model

```bash
python model.py
```

Loads the saved model, runs predictions on test data, and prints evaluation metrics.

---

## 📈 Model Evaluation Metrics

After running `model.py`, you will see:

| Metric | Description |
|---|---|
| **R² Score** | How well the model fits the data (1.0 = perfect) |
| **MAE** | Mean Absolute Error |
| **MSE** | Mean Squared Error |
| **RMSE** | Root Mean Squared Error |

---

## 📦 Requirements

```
numpy
python
VS code
```

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- [ ] Add a web interface using Streamlit
- [ ] Try Ridge and Lasso Regression
- [ ] Add cross-validation
- [ ] Deploy as a REST API

---
