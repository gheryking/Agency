import os
from email.mime.image import MIMEImage
from django.template.loader import render_to_string
import base64

from django.shortcuts import render

from django.http import HttpResponseRedirect # redirect the pages after submit
from django.contrib import messages # REturn messages
from django.core.mail import EmailMultiAlternatives # Required to send emails
from django.template import loader # Render templates on email boy
from .models import Registered_email


# Function to render home page
def home(request):
    return render(request,"home.html")

# Function to render opportunities page
def opportunities(request):
    return render(request, 'opportunities.html')

# ===================> RESUMES <===================

# Function to send email  to frontend opportunities page
def email_frontend(request):
    if request.method == "POST":
        
        # Check if email exists in BD
        email = request.POST['email']
        
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request," We already your resume in our DB")
            return HttpResponseRedirect('/opportunities')
        #=================== =================== ===================
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')
            
            # Register inside DB
            contact = Registered_email()
            contact.email= email
            contact.save()
            
            #=================== =================== ===================            
                        
            template = loader.get_template('resume_form.txt')
            context = {
                'name' : name,
                'age' : age,
                'email' : email,
                'phone' : phone,
                'address' : address,
                'experience' : experience,
                'skills':skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                
                "FrontEnd - Candidate", message,
                "FrontEnd Opportunity",
                ['gerardo.lunarcito@gmail.com']
            )
            email.content_subtype='html'
            file = request.FILES['file']
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, 'FrontEnd resume sent successfully !')
            return HttpResponseRedirect('/')
    
# Function to send email  to backend opportunities page
def email_backend(request):
     if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        
        template = loader.get_template('resume_form.txt')
        context = {
            'name' : name,
            'age' : age,
            'email' : email,
            'phone' : phone,
            'address' : address,
            'experience' : experience,
            'skills':skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            
            "Backend - Candidate", message,
            "Backend Opportunity",
            ['gerardo.lunarcito@gmail.com']
        )
        email.content_subtype='html'
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        messages.success(request, 'Backend resume sent successfully !')
        return HttpResponseRedirect('/')
    

# Function to send email  to fullstack opportunities page
def email_fullstack(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        
        template = loader.get_template('resume_form.txt')
        context = {
            'name' : name,
            'age' : age,
            'email' : email,
            'phone' : phone,
            'address' : address,
            'experience' : experience,
            'skills':skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            
            "Fullstack - Candidate", message,
            "Fullstack Opportunity",
            ['gerardo.lunarcito@gmail.com']
        )
        email.content_subtype='html'
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        messages.success(request, 'Fullstack resume sent successfully !')
        return HttpResponseRedirect('/')
