from django.shortcuts import render
from .front import my_view
# Create your views here.

def login_page(request):
    my_view(request)
    return render(request, 'background_template.html') #didnt pass the template folder name becuase it exists within the application