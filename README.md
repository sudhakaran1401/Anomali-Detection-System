# 🔍 Anomaly Detection Analytics Dashboard (Django + Machine Learning)

## 📌 Overview

This project is a **web-based anomaly detection analytics dashboard** built using **Django and Machine Learning**. It allows users to upload datasets (CSV), analyze them in real-time, and detect unusual patterns (anomalies) using the **Isolation Forest algorithm**.

The system provides **interactive visualizations, filtering options, and downloadable reports**, making it suitable for business data analysis such as payroll monitoring.

---

## 🚀 Key Features

### 📊 Data Upload & Processing

* Upload CSV datasets directly from the UI
* Automatic preprocessing using Pandas
* Handles missing values and small datasets safely

---

### 📈 Analytics Dashboard

* Summary cards:

  * Total Records
  * Normal Records
  * Anomalies Detected
* Clean and responsive UI

---

### 📉 Visualization

* Interactive **line chart** showing anomaly distribution
* Toggle chart visibility
* Separate highlighting for:

  * Normal data
  * Anomalous data

---

### 🔍 Data Filtering & Controls

* Show only anomalies
* Show only normal records
* Reset filters dynamically

---

### 📋 Tabular Data View

* Paginated data table
* Columns include:

  * Employee
  * Department
  * Salary details (Gross, Deduction, Net Pay)
  * Result (Normal / Anomaly)
  * Reason (explanation for anomaly)

---

### 📥 Export Features

* Download processed data as:

  * CSV file
  * PDF report

---

### 🧠 Machine Learning

* Algorithm: **Isolation Forest**
* Contamination: 5%
* Output:

  * `-1` → Anomaly
  * `1` → Normal

---

## 🏗️ Project Architecture

User Upload (CSV)
→ Django Views (`views.py`)
→ Data Processing (Pandas)
→ ML Model (`ml/anamoly.py`)
→ Prediction Results
→ Dashboard UI (Charts + Table + Summary)

---

## 🛠️ Tech Stack

### Backend

* Python
* Django

### Machine Learning

* Pandas
* NumPy
* Scikit-learn

### Frontend

* HTML
* CSS / Bootstrap
* Chart.js

---

## 📂 Project Structure

```
Anomali-Detection-System/
 ├── Anamoly/
 │    ├── ml/
 │    │    └── anamoly.py
 │    ├── views.py
 │    ├── urls.py
 │
 ├── Anamoly_Detection/
 │    ├── settings.py
 │    ├── urls.py
 │
 ├── templates/
 │    ├── home.html
 │    ├── result.html
 │
 ├── manage.py
 ├── requirements.txt
```

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/sudhakaran1401/Anomali-Detection-System.git
cd Anomali-Detection-System

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📊 How It Works

1. Upload a CSV file (e.g., payroll dataset)
2. Data is processed using Pandas
3. Isolation Forest detects anomalies
4. Results are:

   * Displayed in dashboard
   * Visualized using charts
   * Explained with reasons
5. Users can filter and download reports

---

## 📈 Sample Output

* **Total Records:** 32
* **Normal:** 30
* **Anomalies:** 2

Each anomaly includes a **reason**, such as:

> "Gross, Deduction, Net Pay are slightly unusual"

---

## ⚠️ Notes

* Supports only numerical features (current version)
* Database file (`db.sqlite3`) not included
* Designed for small to medium datasets

---

## 🔮 Future Improvements

* Support categorical features
* Model persistence (save/load trained model)
* Multiple algorithm comparison
* User authentication system
* Advanced dashboards (graphs, filters)
* Deployment (Render / AWS)

---

## 👨‍💻 Author

Sudha Karan

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
