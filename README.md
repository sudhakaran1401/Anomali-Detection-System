# 🔍 Anomaly Detection System (Django + Machine Learning)

## 📌 Overview

This project is a web-based anomaly detection system built using Django and Machine Learning. It allows users to input data through a web interface and identifies unusual patterns (outliers) using the Isolation Forest algorithm.

The system performs data preprocessing, handles missing values, and classifies each record as **“Normal”** or **“Anomaly”** with robust error handling to ensure stability.

---

## ⚙️ Features

* Web-based interface for anomaly detection
* Automatic handling of missing values
* Works with small datasets (safe fallback logic)
* Robust error handling to prevent application crashes
* Modular architecture separating ML logic from backend
* Real-time prediction results

---

## 🧠 Tech Stack

### Backend

* Python
* Django

### Machine Learning

* Pandas
* NumPy
* Scikit-learn

### Frontend

* HTML
* Django Templates

---

## 🔬 Algorithm Used

**Isolation Forest**

* Efficient for detecting anomalies in datasets
* Works by isolating outliers instead of profiling normal data
* Configuration:

  * Contamination: 5%
* Output:

  * `-1` → Anomaly
  * `1` → Normal

---

## 🏗️ Project Architecture

User Input (HTML Form)
→ Django Views (`views.py`)
→ ML Module (`ml/anamoly.py`)
→ Isolation Forest Model
→ Prediction Result
→ Display in UI (`result.html`)

---

## 📂 Project Structure

```
Anomali-Detection-System/
 ├── Anamoly/                 # Django App
 │    ├── ml/
 │    │    └── anamoly.py     # ML logic
 │    ├── views.py
 │    ├── urls.py
 │    └── ...
 │
 ├── Anamoly_Detection/       # Project Settings
 │    ├── settings.py
 │    ├── urls.py
 │    └── ...
 │
 ├── templates/
 │    ├── home.html
 │    └── result.html
 │
 ├── manage.py
 ├── requirements.txt
 ├── .gitignore
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/sudhakaran1401/Anomali-Detection-System.git
cd Anomali-Detection-System
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Migrations

```
python manage.py migrate
```

### 5. Run the Server

```
python manage.py runserver
```

---

## 📊 How It Works

1. User inputs data through the web interface
2. Backend processes data using Pandas
3. Isolation Forest model detects anomalies
4. Results are displayed in the UI

---

## 📈 Output

* Displays prediction result:

  * **Anomaly** → Unusual data point
  * **Normal** → Regular data point

---

## ⚠️ Notes

* Database file (`db.sqlite3`) is not included
* Virtual environment (`venv`) is ignored
* Only numerical data is used for predictions

---

## 🔮 Future Improvements

* Support for categorical features
* Feature scaling and preprocessing
* Model comparison (multiple algorithms)
* User authentication system
* Data visualization dashboard

---

## 👨‍💻 Author

Sudha Karan

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
