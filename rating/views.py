from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("welcome to the best website")
