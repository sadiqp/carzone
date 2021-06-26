from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()
    Data = {
        'teams' : teams,
    }
    return render(request,'pages/home.html',Data)

def about(request):
    teams = Team.objects.all()
    Data = {
        'teams' : teams,
    }
    return render(request,'pages/about.html',Data)

def contact(request):
    return render(request,'pages/contact.html')

def services(request):
    return render(request,'pages/services.html')