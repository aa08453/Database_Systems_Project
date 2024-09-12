from django.shortcuts import render
from .front import login_view, register
# Create your views here.

def login_page(request):
    login_view(request)
    return render(request, 'background_template.html') #didnt pass the template folder name becuase it exists within the application

def register_page(request):
    register(request)
    return render(request, 'register.html') #didnt pass the template folder name becuase it exists within the application

def team_page(request):
    return render(request, 'teams.html') #didnt pass the template folder name becuase it exists within the application