from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    else:
        return redirect('users:login')
