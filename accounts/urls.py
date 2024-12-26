# accounts/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'accounts/register.html')  # Ensure the template path is correct

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
