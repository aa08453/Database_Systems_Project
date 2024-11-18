from django.shortcuts import render, redirect
from .front import *
from .forms import BlogForm

# Create your views here.

def login_page(request):
    login_view(request)
    return render(request, 'background_template.html') #didnt pass the template folder name becuase it exists within the application

def register_page(request):
    return (register(request))
    ##use this to redirect to the desired page dont call the render again 
    #return render(request, 'register.html') #didnt pass the template folder name becuase it exists within the application

def team_page(request):
    return redirect('Math_club:register_page') #didnt pass the template folder name becuase it exists within the application


def finance_page(request):
    return render(request, 'finance.html') #didnt pass the template folder name becuase it exists within the application

# In your views.py

def finance_submit(request):
    # Process the submission logic here
    financial(request)
    return render(request, 'finance.html')  # Render the appropriate template or redirect

def voting_poll(request):
    return render(request, 'voting_template.html') #didnt pass the template folder name becuase it exists within the application

def add_product_page(request):
    return add_product(request);


def submit_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # Here, you would typically save the form data to the database
            # For now, just print it or redirect to a success page
            print(form.cleaned_data)
            return redirect('blog_success')  # Redirect after successful submission
    else:
        form = BlogForm()
    
    return render(request, 'submit_blog.html', {'form': form})
