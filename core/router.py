from django.urls import path
from core.api.viewsets import (index_api, Regions, RegionInformation, Fruits, FruitInformation)

urlpatterns = [
    path('', index_api),
    path('region/', Regions.as_view(), name="region_list"),
    path('region/<int:pk>/', RegionInformation.as_view(), name="region_information"),
    path('fruit/', Fruits.as_view(), name="fruit_list"),
    path('fruit/<int:pk>/', FruitInformation.as_view(), name="fruit_information"),
]