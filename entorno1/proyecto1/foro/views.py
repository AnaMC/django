from django.http import HttpResponse
from django.shortcuts import render
# Para poder usar URL
from django.conf.urls import url 
from django.contrib import admin
from django.urls import path
from foro import views


# Create your views here.

def vista(request):
  return HttpResponse('¡Hola mundo!')