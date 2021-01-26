from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, "homepage.html")

def signup(request):
    return render(request, "registration/signup.html")
