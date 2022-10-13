from django.shortcuts import render
from django.http import HttpResponse as response
# Create your views here.

def index(request):
    return response("Hello world!")
