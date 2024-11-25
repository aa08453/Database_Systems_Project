from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.urls import *
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username_try = request.POST.get('username')
        password_try = request.POST.get('password')
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT user_id, name, password, privilege 
                    FROM users 
                    WHERE Name = %s AND Password = %s
                """, [username_try, password_try])
                row = cursor.fetchone()
                
            if row:
                user_id, username, password, privilege = row
                
                # Set session variables
                request.session['username'] = username
                request.session['user_id'] = user_id
                request.session['privilege'] = privilege
                
                return redirect('main_page')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    
    return render(request, 'background_template.html')

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
        # Retrieve common fields from form
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        registration_date = request.POST.get('registration_date')
        account_type = request.POST.get('account_type')

        try:
            with connection.cursor() as cursor:
                if account_type == 'outsider':
                    # Retrieve outsider-specific fields
                    cnic = request.POST.get('cnic')
                    privilege = 0  # Outsiders have a different privilege level
                    
                    # Insert into User table and Outsider table
                    cursor.execute(
                        """
                        INSERT INTO [User] (Name, Password, Contact_Number, RegDate, Privilege)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        [username, password, contact, registration_date, privilege]
                    )
                    user_id = cursor.lastrowid  # Retrieve the auto-generated user_id
                    cursor.execute(
                        """
                        INSERT INTO [Outsider] (User_ID, CNIC)
                        VALUES (%s, %s)
                        """,
                        [user_id, cnic]
                    )
                elif account_type == 'member':
                    # Retrieve member-specific fields
                    major = request.POST.get('major')
                    hu_id = request.POST.get('hu_id')
                    privilege = 1  # Members have a different privilege level

                    # Insert into User table and Member table
                    cursor.execute(
                        """
                        INSERT INTO [User] (Name, Password, Contact_Number, RegDate, Privilege)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        [username, password, contact, registration_date, privilege]
                    )
                    user_id = cursor.lastrowid  # Retrieve the auto-generated user_id
                    cursor.execute(
                        """
                        INSERT INTO [Member] (User_ID, Major, HU_ID)
                        VALUES (%s, %s, %s)
                        """,
                        [user_id, major, hu_id]
                    )
                else:
                    return render(request, 'register.html', {'error': 'Invalid account type.'})

                # Redirect to the main page on successful registration
                return redirect('main_page')

        except Exception as e:
            # Handle errors and display message on failure
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


