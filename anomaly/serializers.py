from rest_framework import serializers
from .models import AnomalyResult

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnomalyResult
        fields = '__all__'