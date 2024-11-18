from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.urls import *



def login_view(request):
    if request.method == 'POST':
        # Retrieve the data from the form fields
        
        input_data = request.POST.get('username')
        password = request.POST.get('password')
        
        print(input_data)
        print(password)
       
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM [USER] WHERE USERNAME = %s AND Pass = %s", [input_data, password])
            row = cursor.fetchone()
            print (row)
            
            check_user = row[1]
            check_pass = row[2]
            
            if input_data == check_user and password == check_pass:
                print("login successful")
            else:
                print("login failed")
            
        except:
            print("an error occured")


def register(request):
    if request.method == 'POST':
        # Retrieve data from form fields
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        registration_date = request.POST.get('registration_date')
        account_type = request.POST.get('account_type')
        privilege = 1 if account_type == "member" else 0

        try:
            with connection.cursor() as cursor:
                # Insert data into the database
                cursor.execute(
                    """
                    INSERT INTO [User] (Name, Password, Contact_Number, RegDate, Privilege) 
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    [username, password, contact, registration_date, privilege]
                )
                print(reverse('Math_club:login_page'))
                return redirect('Math_club:login_page')  # Redirect to login page

        except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'register.html', {'error': 'Failed to register. Please try again.'})

    return render(request, 'register.html')




def financial(request):
    if request.method == 'POST':
        #retrieve data from fields
        donator_name = request.Post.get('name')
        amount = request.Post.get('quantity')
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Donations (DonorName, DonationAmount) VALUES (%s, %s)", [donator_name, amount])
                print("data was inserted")
                
        except Exception as e:
            print("an error occured")
        
    return render(request, 'finance.html') #didnt pass the template folder name becuase it exists within the application


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('item_title')
        price = request.POST.get('item_price')
        # TODO Do something about this 
        # image = request.Post.get()

        print("Data recieved", [name,price])
        try: 
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO [Products] (Product_Name, Price) VALUES (%s, %s)""", [name,price])
                print("Data was inserted (%s, %s)", [name,price])
        except Exception as e:
            print("an error ocurred")
            print(e)

    return render(request, 'additem.html')
