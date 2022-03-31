from django.urls import path
from core.api.viewsets import (index_api, Regions, RegionInformation, Fruits, FruitInformation)

urlpatterns = [
    path('', index_api),
    path('region/', Regions.as_view(), name="Region list"),
    path('region/<int:pk>/', RegionInformation.as_view(), name="Region information"),
    path('fruit/', Fruits.as_view(), name="Fruit list"),
    path('fruit/<int:pk>/', FruitInformation.as_view(), name="Fruit information"),
]