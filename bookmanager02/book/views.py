from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def  index(requests):
    
    return HttpResponse('index')
