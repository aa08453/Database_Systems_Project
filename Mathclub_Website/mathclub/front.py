from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.urls import *
from django.contrib import messages


def teams(request):
    if request.method == "POST":
        team_name = request.POST.get("team-name")
        team_lead = request.POST.get("team-lead")
        date_created = request.POST.get("creation-date")
        print(team_name)
        
        try:
            print("HI")
            cursor = connection.cursor()
            cursor.execute(
                    """
                    INSERT INTO Teams (Team_Name, Team_Lead, Date_Created) 
                    VALUES (%s, %s, %s)
                    """,
                    [team_name, team_lead, date_created]
                )
            print("insertion is done")
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
    return render(request, "teams.html")


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
    has_privilege = request.session.get('privilege') == 1

    # Pass session data to the template
    return render(request, 'main_page.html', {'user_id': user_id, 'username': username, 'has_privilege': has_privilege}) 


def register(request):
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


