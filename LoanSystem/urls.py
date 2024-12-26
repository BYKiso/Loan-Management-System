from django.contrib import admin
from django.urls import path
from accounts import views  # Import views from the accounts app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.home, name='home'),  # Home page URL
    path('register/', views.register, name='register'),  # Register page URL
    path('login/', views.login_view, name='login'),  # Login page URL
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard page URL
]
