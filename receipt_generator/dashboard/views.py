from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import User
from .forms import LoginForm, RegisterForm


def index(request):
    return redirect('login')


def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')


def register(request):
    form = RegisterForm()