from django.urls import path,include
from core.api.viewsets import (index, Regions, RegionInformation, Fruits, FruitInformation)


from rest_framework import routers
from core.api import viewsets as fruitlibraryviewsets
#criando nosso objeto de rota
route = routers.DefaultRouter()
route.register(r'regions', fruitlibraryviewsets.RegionViewSet, basename="Regions")
route.register(r'fruits', fruitlibraryviewsets.FruitViewSet, basename="Fruits")



urlpatterns = [
    
    path('api_root/', include(route.urls)),
    path('', index),
    path('region/', Regions.as_view(), name="region_list"),
    path('region/<int:pk>/', RegionInformation.as_view(), name="region_information"),
    path('fruit/', Fruits.as_view(), name="fruit_list"),
    path('fruit/<int:pk>/', FruitInformation.as_view(), name="fruit_information"),
]