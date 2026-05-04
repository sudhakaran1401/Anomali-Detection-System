import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    try:
    # Select numeric columns
        numeric_df = df.select_dtypes(include=['int64', 'float64'])

            # 🚨 Case 1: No numeric data
        if numeric_df.empty:
            df['result'] = "Normal"
            return df

            # 🚨 Case 2: Handle missing values
        numeric_df = numeric_df.fillna(numeric_df.mean())

            # 🚨 Case 3: Too few rows
        if len(numeric_df) < 2:
            df['result'] = "Normal"
            return df

            # Model
        model = IsolationForest(contamination=0.05, random_state=42)

        predictions = model.fit_predict(numeric_df)

        df['result'] = ["Anomaly" if x == -1 else "Normal" for x in predictions]

        return df

    except Exception as e:
        print("ML ERROR:", e)

        # NEVER crash UI
        df['result'] = "Normal"
        return df

