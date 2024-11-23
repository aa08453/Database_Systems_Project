from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.urls import *



def login_view(request):
    if request.method == 'POST':
        # Retrieve the data from the form fields
        
        input_data = request.POST.get('username')
        password = request.POST.get('password')
         
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM [USER] WHERE Name = %s AND Password = %s", [input_data, password])
            row = cursor.fetchone()
            print (row)
            
            check_user = row[1]
            check_pass = row[5]
            print(check_user)
            print(check_pass)
            
            if input_data == check_user and password == check_pass:
                print("login successful")
                request.session['username'] = check_user
                request.session['userid'] = row[0]
                
                return redirect('Math_club:main_page')
            else:
                print("login failed")
            
        except:
            print("an error occured")
    return render(request, 'background_template.html') #didnt pass the template folder name becuase it exists within the application

def main_view(request):
    # Retrieve userid and username from the session
    userid = request.session.get('userid')
    username = request.session.get('username')

    # Check if session data exists; if not, redirect to the login page
    if not userid or not username:
        return redirect('Math_club:login_page')

    print(f"UserID: {userid}, Username: {username}")

    # Pass session data to the template
    return render(request, 'main_page.html', {'userid': userid, 'username': username})



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

#========================= TAGS ==================================================

def create_tag(request):
    if request.method == 'POST':
        tagname = request.POST.get('tagname')
        try:
            with connection.cursor() as cursor:
                # Insert data into the database
                cursor.execute(
                    """
                    INSERT INTO [Tags] (Name) 
                    VALUES (%s) """, [tagname]
                )
                print('Tag created')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    return render(request, 'tags/create.html')

def create_club_item(request):
    if request.method == 'POST':
        itemname = request.POST.get('itemname')
        storage = request.POST.get('storage')
        person_responsible = request.POST.get('person_responsible')
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT [Item_Name] [Storage] VALUES (%s) (%s)
                    """, [itemname] [storage]
                )
                print('CLub item created')
        except Exception as e:
            print(f"An error occurred: {e}")
    return render(request, 'club_items/create.html')
    
