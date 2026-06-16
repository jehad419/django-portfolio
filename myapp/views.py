from django.shortcuts import render
from django.http import HttpResponse

#Home page
def home(request):
    return render(request , 'home.html')

#About page
def about(request):
    return render(request , 'about.html')

#Projects page
def projects(request):
    return render(request , 'projects.html')

#Skills page
def skills(request):
    return render(request , 'skills.html')

# Contact page
def contact(request):
    return render(request , 'contact.html')