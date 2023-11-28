from rest_framework import serializers
from .models import InGreenhouse, Temperature
from rest_framework import serializers

class InGreenhouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InGreenhouse
        fields = '__all__'

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'
