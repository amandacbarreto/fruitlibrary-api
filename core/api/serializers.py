from rest_framework import serializers
from core import models

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fruit
        fields = '__all__'