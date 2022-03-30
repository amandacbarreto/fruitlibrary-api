from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def region(request):
    return HttpResponse('Página de region')

def fruit(request):
    return HttpResponse('Página de fruit')