# 🔍 Anomaly Detection System

## 📌 Overview

This project is a machine learning-based anomaly detection system developed using Python. It identifies unusual patterns (outliers) in datasets by applying the Isolation Forest algorithm.

The system processes input data, handles missing values, and classifies each record as **“Normal”** or **“Anomaly”**, ensuring robust and reliable predictions.

---

## ⚙️ Features

* Anomaly detection in numerical datasets with auto handling missing values
* Works with small datasets (safe fallback handling)
* Robust error handling to prevent application crashes
* Web interface using Django or Flask
* Visualization dashboard for insights

---

## 🧠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn

---

## 🔬 Algorithm Used

**Isolation Forest**

* Efficient algorithm for anomaly detection
* Works by isolating outliers instead of profiling normal points
* Output labels:

  * `-1` → Anomaly
  * `1` → Normal

---

## 📂 Project Structure

```
Anomali-Detection-System/
 ├── detect.py
 ├── requirements.txt
 ├── README.md
 └── .gitignore
```

---

## 🚀 How to Run

### 1. Clone the Repository

```
git clone https://github.com/sudhakaran1401/Anomali-Detection-System.git
cd Anomali-Detection-System
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Project

```
python detect.py
```

---

## 📊 Input

* Accepts a dataset (Pandas DataFrame)
* Only numerical columns are used for detection
* Missing values are handled automatically

---

## 📈 Output

* Adds a new column: `result`
* Values:

  * `"Anomaly"` → Unusual data point
  * `"Normal"` → Regular data point

---

## ⚠️ Notes

* Dataset files are not included in this repository
* You can use your own CSV dataset
* Designed for learning and demonstration purposes

---

## 🔮 Future Improvements

* Support for categorical features
* Feature scaling and preprocessing enhancements
* Model performance tuning
* User Authentication
* Model Comparisions


---

## 👨‍💻 Author

Sudha Karan

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
