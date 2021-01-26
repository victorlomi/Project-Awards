from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm

def homepage(request):
    return render(request, "homepage.html")

def signup(request):
    form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
