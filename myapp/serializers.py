from rest_framework import serializers
from .models import InGreenhouse, Greenhouse
from rest_framework import serializers

class InGreenhouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InGreenhouse
        fields = '__all__'

class GreenhouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greenhouse
        fields = '__all__'
