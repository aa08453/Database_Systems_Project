from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.urls import *



def login_view(request):
    if request.method == 'POST':
        # Retrieve the data from the form fields
        
        username_try = request.POST.get('username')
        password_try = request.POST.get('password')
         
        try:
            cursor = connection.cursor()
            cursor.execute("""select user_id, name, password, privilege FROM
            users WHERE Name = %s AND Password = %s""", [username_try, password_try])
            row = cursor.fetchone()
            print(row)
            if (row is None):
                print("No such user exists") #TODO: Make this a more convincing message w redirect
                return
            user_id = row[0]
            username = row[1]
            password = row[2]
            privilege = row[3]
            
            if username_try == username and password_try == password:
                print("login successful")
                request.session['username'] = username 
                request.session['user_id'] = user_id
                request.session['privilege'] = privilege
                
                return redirect('main_page')
            else:
                print("login failed")
            
        except Exception as e:
            print("an error occured")
            print(username_try)
            print(password_try)
            print(e)
    return render(request, 'background_template.html') #didnt pass the template folder name becuase it exists within the application

def main_view(request):
    # Retrieve userid and username from the session
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    # Check if session data exists; if not, redirect to the login page
    if not user_id or not username:
        return redirect('Math_club:login_page')

    print(f"UserID: {user_id}, Username: {username}")

    # Pass session data to the template
    return render(request, 'main_page.html', {'user_id': user_id, 'username': username})



def register(request):
    if request.method == 'POST':
        # Retrieve data from form fields
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        registration_date = request.POST.get('registration_date')
        account_type = request.POST.get('account_type')
        privilege = 1 if account_type == "member" else 0 #TODO: Add more logic to update privilege

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
            print("An error ocurred while inserting a product")
            print(e)

    return render(request, 'additem.html')


