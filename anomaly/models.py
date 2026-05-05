from django.db import models

class AnomalyResult(models.Model):
    file_name = models.CharField(max_length=100)
    total = models.IntegerField()
    normal = models.IntegerField()
    anomalies = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name