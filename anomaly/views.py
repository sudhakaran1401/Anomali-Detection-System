import csv
from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render
from anomaly.models import AnomalyResult
from .ml.anomaly import detect_anomalies
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AnomalyResult
from .serializers import AnomalySerializer
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def home(request):
    if request.method == "POST" and request.FILES.get("file"):

        file = request.FILES["file"]

        try:
            df = pd.read_csv(file)

            # Detect anomalies
            result_df = detect_anomalies(df)

            # --------- IMPROVEMENT 1: Add Reason ----------
            def explain_anomaly(row, df):
                unusual_cols = []

                for col in df.select_dtypes(include=['number']).columns:
                    mean = df[col].mean()
                    std = df[col].std()

                    if std != 0:
                        deviation = abs(row[col] - mean) / std

                        if deviation > 0.5:
                            unusual_cols.append(col)

                # 🔥 IMPROVED LOGIC
                if row.get("result") == "Anomaly":
                    if len(unusual_cols) == 1:
                        return f"{unusual_cols[0]} is slightly unusual"

                    elif len(unusual_cols) > 1:
                        cols = ", ".join(unusual_cols)
                        return f"({cols}) are slightly unusual"

                    else:
                        return "Unusual pattern detected by ML model"

                return "Within normal range"


            result_df['reason'] = result_df.apply(lambda row: explain_anomaly(row, result_df), axis=1)

            # --------- IMPROVEMENT 2: Faster Data Conversion ----------
            data = result_df.to_dict(orient='records')
            columns = list(result_df.columns)

            total = len(result_df)

            anomalies = len(result_df[result_df['result'] == 'Anomaly']) if 'result' in result_df.columns else 0
            normal = total - anomalies

            AnomalyResult.objects.create(
                file_name=file.name,   # 👈 use file.name (NOT filename variable)
                total=total,
                normal=normal,
                anomalies=anomalies
            )

            # --------- IMPROVEMENT 3: Scatter Plot Data ----------
            numeric_cols = result_df.select_dtypes(include=['number']).columns

            scatter_data = []
            if len(numeric_cols) >= 2:
                x_col = numeric_cols[0]
                y_col = numeric_cols[1]

                for _, row in result_df.iterrows():
                    scatter_data.append({
                        "x": row[x_col],
                        "y": row[y_col],
                        "label": row.get("result", "Normal")
                    })

            request.session['results'] = data
            request.session['columns'] = columns

            return render(request, "result.html", {
                "columns": columns,
                "data": data,
                "total": total,
                "anomalies": anomalies,
                "normal": normal,
                "scatter_data": scatter_data,
                "filename": file.name
            })

        except Exception as e:
            print("VIEW ERROR:", e)
            return render(request, "home.html", {
                "error": f"Error processing file: {str(e)}"
            })

    return render(request, "home.html")

def download_csv(request):
    data = request.session.get('results', [])
    columns = request.session.get('columns', [])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results.csv"'

    writer = csv.writer(response)

    if columns:
        writer.writerow(columns)

    for row in data:
        writer.writerow([row.get(col, "") for col in columns])

    return response

@api_view(['GET'])
def get_results(request):
    data = AnomalyResult.objects.all().order_by('-created_at')
    serializer = AnomalySerializer(data, many=True)
    return Response(serializer.data)

def download_pdf(request):
    data = request.session.get('results', [])

    filter_type = request.GET.get('filter')

    # 🔥 Apply filter
    if filter_type == "normal":
        data = [row for row in data if row.get('result') == 'Normal']
    elif filter_type == "anomaly":
        data = [row for row in data if row.get('result') == 'Anomaly']

    total = len(data)
    anomalies = len([row for row in data if row.get('result') == 'Anomaly'])
    normal = total - anomalies

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("Anomaly Detection Report", styles['Title']))
    content.append(Paragraph(f"Total: {total}", styles['Normal']))
    content.append(Paragraph(f"Normal: {normal}", styles['Normal']))
    content.append(Paragraph(f"Anomalies: {anomalies}", styles['Normal']))

    doc.build(content)
    return response