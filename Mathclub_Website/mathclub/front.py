from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection




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
        #retrieve data from fields
        input_data = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO [USER] (USERNAME, Pass) VALUES (%s, %s)", [input_data, password])
                print("data was inserted")
                
        except Exception as e:
            print("an error occured")
        


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
