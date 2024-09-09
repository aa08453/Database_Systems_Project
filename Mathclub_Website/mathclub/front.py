from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def my_view(request):
    if request.method == 'POST':
        # Retrieve the data from the form fields
        
        input_data = request.POST.get('username')
        password = request.POST.get('password')
        
        # Do something with the input data
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO [USER] (username, password) VALUES (%s, %s)", [input_data, password])
                
            return HttpResponse('Data retrieved successfully!')

        except Exception as e:
            return HttpResponse('An error occurred while retrieving the data!')
    
    
    return render(request, 'background_template.html')