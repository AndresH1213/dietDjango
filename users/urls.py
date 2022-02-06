from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login')
]