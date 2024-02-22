from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse("<h1>Hello world! Your project is running successfully</h1")
