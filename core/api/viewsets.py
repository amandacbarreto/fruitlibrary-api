from rest_framework import viewsets
from core.api import serializers
from core import models

class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegionSerializer
    queryset = models.Region.objects.all()

class FruitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FruitSerializer
    queryset = models.Fruit.objects.all()