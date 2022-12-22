from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name="home"),
    
    # OPPORTUNITIES
    path('opportunities/', views.opportunities, name='opportunities'),
    
    # ===================> SEND EMAILS <===================
    
    #   PATH TO SEND frontTEND FORM
    path('email_frontend', views.email_frontend, name='email_frontend'),
    #   PATH TO SEND backEND FORM
    path('email_backend', views.email_backend, name='email_backend'),
    #   PATH TO SEND fullStack FORM
    path('email_fullstack', views.email_fullstack, name='email_fullstack'),
]
