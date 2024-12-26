# accounts/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'accounts/register.html')

def login_view(request):
    return render(request, 'accounts/login.html')  # Render the login template


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Home view
def home(request):
    return render(request, 'home.html')


# Register view
def register(request):
    return render(request, 'accounts/register.html')


# Login view
def login_view(request):
    if request.method == "POST":
        # Get email and password from POST request
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Login the user and redirect to the dashboard
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            # If authentication fails, show error message
            messages.error(request, "Invalid email or password.")

    return render(request, 'accounts/login.html')


# Dashboard view (after successful login)
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')  # Render the dashboard template

