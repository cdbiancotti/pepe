from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Perro

# Create your views here.

def index(request):
    next_dog = Perro.objects.count()
    perro = Perro.objects.create(nombre=f'perro {next_dog}')
    return HttpResponse(f'{perro}')