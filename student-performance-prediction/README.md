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
├── train.py          # Model training script
├── test.py           # Model testing and evaluation script
├── dataset.csv       # Student dataset
├── model.pkl         # Saved trained model (generated after training)
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
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
| `sleep_hours` | Average daily sleep hours |
| **`final_score`** | **Target — final exam score** |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-performance-prediction.git
cd student-performance-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Usage

### Train the Model

```bash
python train.py
```

Loads the dataset, trains the Linear Regression model, and saves it as `model.pkl`.

### Test the Model

```bash
python test.py
```

Loads the saved model, runs predictions on test data, and prints evaluation metrics.

---

## 📈 Model Evaluation Metrics

After running `test.py`, you will see:

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
pandas
scikit-learn
matplotlib
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

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Your Name**  
GitHub: [@your-username](https://github.com/your-username)

---

*If you found this helpful, give it a ⭐ on GitHub!*
