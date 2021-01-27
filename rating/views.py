from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import *
from .forms import SignUpForm, AddProjectForm
from .models import Project
from django.contrib.auth import logout

def homepage(request):
    return render(request, "homepage.html")

def profile(request):
    return render(request, "profile.html")

def add_project(request):
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = Project(title=form.cleaned_data.get('title'),
                              photo=form.cleaned_data.get('photo'),
                              description=form.cleaned_data.get('description'),
                              link=form.cleaned_data.get('link'),
                              user=request.user)
            project.save()
            return redirect('homepage')
        else:
            return render(request, 'add-project.html', {'form': form})
    else:
        form = AddProjectForm()
        return render(request, 'add-project.html', {'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print("handling signup")
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.profile_photo = form.cleaned_data.get('profile_photo')
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print("signed up")
            return redirect('homepage')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
