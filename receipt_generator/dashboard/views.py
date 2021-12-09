from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import User
from .forms import LoginForm


def index(request):
    return redirect('login')


def login(request):
    return render(request, 'registration/login.html')