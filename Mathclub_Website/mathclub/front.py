from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    if request.method == 'POST':
        # Retrieve the data from the form fields
        
        input_data = request.POST.get('username')
        password = request.POST.get('password')
        
        # Do something with the input data
                
        return HttpResponse('Data retrieved successfully!')
    
    
    return render(request, 'my_template.html')