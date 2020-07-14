from rest_framework import serializers
from .models import Temperature_Measure

class Temperature_MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature_Measure
        fields = '__all__'