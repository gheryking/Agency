from django.shortcuts import render

from django.http import HttpResponseRedirect # redirect the pages after submit
from django.contrib import messages # REturn messages
from django.core.mail import EmailMultiAlternatives # Required to send emails
from django.template import loader # Render templates on email boy


# Function to render home page
def home(request):
    return render(request,"home.html")

# Function to render opportunities page
def opportunities(request):
    return render(request, 'opportunities.html')

# Function to send email  to frontend opportunities page
def email_frontend(request):
    pass

# Function to send email  to backend opportunities page
def email_backend(request):
    pass

# Function to send email  to fullstack opportunities page
def email_fullstack(request):
    pass
