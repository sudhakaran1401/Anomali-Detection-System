import pandas as pd
from django.shortcuts import render
from .ml.anamoly import detect_anomalies

def home(request):
    if request.method == "POST" and request.FILES.get("file"):

        file = request.FILES["file"]

        try:
            # Read CSV safely
            df = pd.read_csv(file)

            # Run anomaly detection (safe)
            result_df = detect_anomalies(df)

            # Convert for template
            columns = list(result_df.columns)

            data = []
            for _, row in result_df.iterrows():
                data.append([row[col] for col in columns])

            total = len(result_df)

            # Safe anomaly count
            if 'result' in result_df.columns:
                anomalies = len(result_df[result_df['result'] == 'Anomaly'])
            else:
                anomalies = 0

            normal = total - anomalies

            return render(request, "result.html", {
                "columns": result_df.columns,
                "data": data,
                "total": total,
                "anomalies": anomalies,
                "normal": normal
            })

        except Exception as e:
            print("VIEW ERROR:", e)

            return render(request, "home.html", {
                "error": f"Error processing file: {str(e)}"
            })

    return render(request, "home.html")
