from django.shortcuts import render, redirect
from .front import *
from django.contrib import messages
from datetime import datetime
from .myutils import *

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, FormView, DeleteView, View
from django.urls import reverse_lazy

from .forms import *
# Create your views here.

def main_page(request):
    return main_view(request)


def login_page(request):
    return login_view(request)

def register_page(request):
    return (register(request))

def team_page(request):
    return teams(request)


def finance_page(request):
    return render(request, 'finance.html') 

# In your views.py

def finance_submit(request):
    # Process the submission logic here
    financial(request)
    return render(request, 'finance.html')  # Render the appropriate template or redirect

def voting_poll(request):
    return render(request, 'voting_template.html') #didnt pass the template folder name becuase it exists within the application

def add_product_page(request):
    return add_product(request)


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



def election_create_page(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        print(start_date.replace("T", " "))
        print(end_date.replace("T", " "))


        try:
            with connection.cursor() as cursor:
                cursor.execute(""" insert into elections (start_date, end_date)
                values (%s, %s) """, [start_date.replace("T", " "),
                                      end_date.replace("T", " ")])
        except Exception as e:
            print("An error occurred while adding an election")
            print(e)

    election = fetch_elections()
    return render(request, 'election/create.html', {"election" : election})


def election_retrieve_page(request):
    elections = fetch_elections()
    user_privilege = request.session["privilege"]
    print("User has privs", user_privilege)
    user_has_permission = (user_privilege == 1)


    return render(request, 'election/retrieve.html', {'elections': elections,
                  'user_has_permission' : user_has_permission})


def election_update_page(request):
    return

def election_delete_page(request):
    return


def finance_update_page(request):
    return

class GenericListView(ListView):
    template_name = "list_page.html" 
    sql = None
    pk_field = ""

    #TODO: Make a insertion check hook
    #TODO: Make cascade deletion 
    #TODO: Make error messages


    def get_search_field(self):
        return self.request.GET.get("search_field", "name")

    def get_queryset(self, query=""):
        search_field = self.get_search_field()
        sql = self.sql
        with connection.cursor() as cursor:
            if query:
                sql += f"where {search_field} like %s"
                cursor.execute(sql, [f"%{query}%"])
            else:
                cursor.execute(sql)

            columns = [col[0] for col in cursor.description]
            for x in range(0, len(columns)):
                if columns[x] == self.pk_field:
                    columns[x] = "pk_field"
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return columns, rows
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")

        columns,items = self.get_queryset(query)
        context["items"] = items
        context["columns"] = columns
        context["table_name"] = self.table_name
        context["create_url"] = f"/{self.table_name}/create/"
        context["update_url"] = f"/{self.table_name}/update/"
        context["delete_url"] = f"/{self.table_name}/delete/"
        user_privilege = self.request.session.get("privilege", None)

        context["has_privilege"] = user_privilege == 1  # Only show actions if privilege is 1
        return context

class GenericPageView(TemplateView): #Create/update in one go
    template_name = "form_page.html"
    table_name = None
    fields = []
    pk_field = ""
    redirect_to = ""
    form_class = None


    def get_object(self, pk):
        with connection.cursor() as cursor:
            sql = f"select * from {self.table_name} where {self.pk_field} = %s"
            cursor.execute(sql, [pk])
            row = cursor.fetchone()
            if (row is not None):
                columns = [col[0] for col in cursor.description]
                return dict(zip(columns,row))
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk", None)
        print("I've got pk", pk)
        context["object"] = self.get_object(pk) if pk else None
        context["fields"] = self.fields
        user_privilege = self.request.session.get("privilege", None)
        user_id = self.request.session.get("user_id", None)
        print("The user id is ", user_id)
        context["user_id"] = user_id
        context["has_privilege"] = user_privilege == 1  # Only show actions if privilege is 1

        obj = self.get_object(pk) if pk else None
        initial_data = {key: value for key, value in obj.items() if key != self.pk_field} if obj else None
        print(self.form_class)
        context["form"] = self.form_class(initial=initial_data) if obj else self.form_class()
        print("The form with context is ", context["form"].fields)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(f"Current class: {self.__class__.__name__}")  # Debug the class name
        if form.is_valid(): #If valid do the thing
            data = form.cleaned_data
            pk = self.kwargs.get("pk")
            with connection.cursor() as cursor:
                if pk: #in this case we are updating
                    set_clause = ", ".join([f"{field} = %s" for field in self.fields])
                    sql = f"update {self.table_name} set {set_clause} where {self.pk_field} = %s"
                    cursor.execute(sql, list(data.values()) + [pk])
                else:
                    columns = ", ".join(self.fields)
                    placeholders = ", ".join(["%s"] * len(self.fields))
                    sql = f"insert into {self.table_name} ({columns}) values ({placeholders})"
                    cursor.execute(sql, list(data.values()))

            return redirect(self.redirect_to)
        return render(request, self.template_name, {'form' : form}) #Otherwise ask again



from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.db import IntegrityError

class GenericDeleteView(View):
    table_name = None
    pk_field = ""
    redirect_to = ""

    def post(self, request, pk=None):
        if not pk:
            return HttpResponseNotFound("Record not found: Missing primary key.")

        try:
            with connection.cursor() as cursor:
                # Perform the delete operation
                sql = f"DELETE FROM {self.table_name} WHERE {self.pk_field} = %s"
                cursor.execute(sql, [pk])
            return redirect(self.redirect_to)
        except IntegrityError as e:
            # Handle foreign key constraint violations or other database integrity issues
            return HttpResponse(
                f"Cannot delete record due to related data: {e}",
                status=400,
            )
        except Exception as e:
            # Catch all other exceptions
            return HttpResponse(
                f"An error occurred while deleting the record: {e}",
                status=500,
            )

# Elections
    
class ElectionsListView(GenericListView):
    table_name = "elections"
    sql = """
select Election_ID, Start_Date, End_Date from Elections 
"""
    pk_field = "Election_ID"



# Candidates

class CandidatesListView(GenericListView):
    table_name = "candidates"
    sql = """
select Candidate_ID, R.Role_Name as Role_Name, E.Start_Date as Start_Date, E.End_Date as End_Date, U.Name as Name
from Candidates C 
join Role_Types R on R.Role_ID = C.Role_ID 
join Elections E on E.Election_ID = C.Election_ID
join Users U on U.User_ID = C.User_ID
    """
    pk_field = "Candidate_ID"

class CandidatesPageView(GenericPageView):
    table_name = "candidates"
    search_field = "Candidate_ID"
    fields = ["Role_ID", "Election_ID", "User_ID"]
    pk_field = "Candidate_ID"
    redirect_to = "list_candidates"
    form_class = candidates_form

class CandidatesDeleteView(GenericDeleteView):
    table_name = "candidates"
    pk_field = "Candidate_ID"
    redirect_to = "list_candidates"

# Role_Types
class Role_TypesListView(GenericListView):
    table_name = "Role_Types"
    sql = """
    select Role_ID, Role_Name
    from Role_Types
    """
    pk_field = "Role_ID"

class Role_TypesPageView(GenericPageView):
    table_name = "Role_Types"
    search_field = "Role_ID"
    fields = ["Role_Name"]
    pk_field = "Role_ID"
    redirect_to = "list_Role_Types"
    form_class = Role_Types_form

class Role_TypesDeleteView(GenericDeleteView):
    table_name = "Role_Types"
    pk_field = "Role_ID"
    redirect_to = "list_Role_Types"

# Locations
class Locations_ListView(GenericListView):
    table_name = "Locations"
    sql = """
    select Location_ID, Location_Name
    from Locations
    """
    pk_field = "Location_ID"

class Locations_PageView(GenericPageView):
    table_name = "Locations"
    search_field = "Location_ID"
    fields = ["Location_Name"]
    pk_field = "Location_ID"
    redirect_to = "list_locations"
    form_class = Locations_form

class Locations_DeleteView(GenericDeleteView):    # delete constraint 
    # need to delete from tables where it is referred to as FK
    table_name = "Locations"
    pk_field = "Location_ID"
    redirect_to = "list_locations"
    
# Majors
class Majors_ListView(GenericListView):
    def __init__(self):
        super().__init__()

    table_name = "Majors"
    sql = """
    select Major_ID, Name
    from Majors
    """
    pk_field = "Major_ID"


class Majors_PageView(GenericPageView):
    table_name = "Majors"
    search_field = "Major_ID"
    fields = ["Name"]
    pk_field = "Major_ID"
    redirect_to = "list_majors"
    form_class = Majors_form

class Majors_DeleteView(GenericDeleteView):
    table_name = "Majors"
    pk_field = "Major_ID"
    redirect_to = "list_majors"
    
# Tags

class Tags_ListView(GenericListView):
    table_name = "Tags"
    sql = """
    select Tag_ID, Tag_Name
    from Tags
    """
    pk_field = "Tag_ID"

class Tags_PageView(GenericPageView):
    table_name = "Tags"
    search_field = "Tag_ID"
    fields = ["Tag_Name"]
    pk_field = "Tag_ID"
    redirect_to = "list_tags"
    form_class = Tags_form

class Tags_DeleteView(GenericDeleteView):
    table_name = "Tags"
    pk_field = "Tag_ID"
    redirect_to = "list_tags"
    
# Products
class Products_ListView(GenericListView):
    table_name = "Products"
    sql = """
    select Product_ID, Product_Name, Price, Items_In_Stock
    from Products
    """
    pk_field = "Product_ID"

# add an option to add to cart/order for users without privilege 
class Products_PageView(GenericPageView):
    table_name = "Products"
    search_field = "Product_ID"
    fields = ["Product_Name", "Price", "Items_In_Stock"]
    pk_field = "Product_ID"
    redirect_to = "list_products"
    form_class = Products_form

class Products_DeleteView(GenericDeleteView):
    table_name = "Products"
    pk_field = "Products_ID"
    redirect_to = "list_products"
    
# Events
class Events_ListView(GenericListView):
    table_name = "Events"
    sql = """
    select E.Event_ID, U.Name, E.Event_Name, E.Start_Date, E.End_Date, L.Location_Name, E.Scale, E.Description
    from Events E join Users U on E.Event_Lead = U.User_ID join Locations L on E.Location = L.Location_ID
    """
    pk_field = "Event_ID"

class Events_PageView(GenericPageView):
    table_name = "Events"
    search_field = "Event_ID"
    fields = ["Event_Name", "Event_Lead", "Start_Date", "End_Date", "Location", "Scale", "Description"]
    pk_field = "Event_ID"
    redirect_to = "list_events"
    form_class = Events_form

class Events_DeleteView(GenericDeleteView):
    table_name = "Events"
    pk_field = "Event_ID"
    redirect_to = "list_events"
    
# Club_Items

class Club_Items_ListView(GenericListView):
    table_name = "Club_Items"
    sql = """
    select C.Item_ID, C.Item_Name, L.Location_Name as Storage
    from Club_Items C join Locations L on C.Storage = L.Location_ID
    """
    pk_field = "Item_ID"

class Club_Items_PageView(GenericPageView):
    table_name = "Club_Items"
    search_field = "Item_ID"
    fields = ["Item_Name", "Storage"]
    pk_field = "Item_ID"
    redirect_to = "list_club_Items"
    form_class = Club_Items_form

class Club_Items_DeleteView(GenericDeleteView):
    table_name = "Club_Items"
    pk_field = "Item_ID"
    redirect_to = "list_club_Items"
    
# Transaction_Types

class Transaction_Types_ListView(GenericListView):
    table_name = "Transaction_Types"
    sql = """
    select Type_ID, Type_Name
    from Transaction_Types
    """
    pk_field = "Type_ID"

class Transaction_Types_PageView(GenericPageView):
    table_name = "Transaction_Types"
    search_field = "Type_ID"
    fields = ["Type_Name"]
    pk_field = "Type_ID"
    redirect_to = "list_tags"
    form_class = Transaction_Types_form

class Transaction_Types_DeleteView(GenericDeleteView):
    table_name = "Transaction_Types"
    pk_field = "Tag_ID"
    redirect_to = "list_tags"
    
class Members(GenericPageView):
    table_name = "Users"
    search_field = "User_ID"
    fields = ["Major", "Name", "Contact_Number", "Reg_Date", "Password", "HUID", "Privilege"]
    pk_field = "User_ID"
    redirect_to = "login_page"
    form_class = Major_choice
    
class Outsiders(GenericPageView):
    table_name = "Users"
    search_field = "User_ID"
    fields = ["Name", "Contact_Number", "Reg_Date", "CNIC", "Address","Privilege","Password"]
    pk_field = "User_ID"
    redirect_to = "login_page"
    form_class = Outsider

class Admins(GenericPageView):
    table_name = "Users"
    search_field = "User_ID"
    fields = ["Name", "Contact_Number", "Reg_Date", "CNIC", "Address","Privilege"]
    pk_field = "User_ID"
    redirect_to = "login_page"
    form_class = Admins





# Blogs

class Blogs_ListView(GenericListView):
    table_name = "Blogs"
    sql = """
    select b.Post_ID, b.Title, b.Date_Created, u.Name as Author, t.Tag_Name
    from Blogs b inner join Users u on u.User_ID = b.User_ID
    inner join Tags t on t.Tag_ID = b.Tag_ID
    """
    pk_field = "Post_ID"

class Blogs_PageView(GenericPageView):
    table_name = "Blogs"
    search_field = "Post_ID"
    fields = ["Title", "Date_Created", "Content","User_ID","Tag_ID"]
    pk_field = "Post_ID"
    redirect_to = "list_blogs"
    form_class = Blogs_form

class Blogs_DeleteView(GenericDeleteView):
    table_name = "Blogs"
    pk_field = "Post_ID"
    redirect_to = "list_blogs"

class ElectionsPageView(GenericPageView):
    table_name = "elections"
    search_field = "start_date"
    fields = ["start_date", "end_date"]
    pk_field = "Election_ID"
    redirect_to = "list_elections"
    form_class = election_form

class ElectionsDeleteView(GenericDeleteView):
    table_name = "elections"
    pk_field = "Election_ID"
    redirect_to = "list_elections"



class Finance_PageView(GenericPageView):
    table_name = "Finances"
    search_field = "Transaction_ID"
    fields = ["Responsible_Officer","User_ID","Transaction_Type","Date","Description","Amount"]
    pk_field = "Transaction_ID"
    redirect_to = "list_Finance"
    form_class = Finances
   
class Finance_ListView(GenericListView):
    table_name = "Finances"
    sql = """
    select Transaction_ID, Responsible_Officer, User_ID, Transaction_Type, Date, Description, Amount FROM Finances
    """ 
    pk_field = "Transaction_ID"
    

class Finance_DeleteView(GenericDeleteView):
    table_name = "Finances"
    pk_field = "Transaction_ID"
    redirect_to = "list_Finance"
    
    

class Teams(GenericPageView):
    table_name = "Teams"
    search_field = "Team_ID"
    fields = ["Team_Name", "Team_Lead", "Date_Created"]
    pk_field = "Team_ID"
    redirect_to = "list_Teams"
    form_class = teams
    
    
class Teams_ListView(GenericListView):
    table_name = "Teams"
    sql = """
    select Team_ID, Team_Name, Team_Lead, Date_Created FROM Teams
    """
    pk_field = "Team_ID"
    
    
class Teams_DeleteView(GenericDeleteView):
    table_name = "Teams"
    pk_field = "Team_ID"
    redirect_to = "list_Teams"
    
    
class Team_Roles(GenericPageView):
    table_name = "Team_Roles"
    search_field = "Role_ID"
    fields = ["Role_Name","Role_Description"]
    pk_field = "Role_ID"
    redirect_to = "list_Roles"
    form_class = Team_Roles_form

class List_Roles(GenericListView):
    table_name = "Team_Roles"
    sql = """
    select Role_ID, Role_Name, Role_Description FROM Team_Roles
    """
    pk_field = "Role_ID"
    
class Team_Roles_DeleteView(GenericDeleteView):
    table_name = "Team_Roles"
    pk_field = "Role_ID"
    redirect_to = "list_Roles"
    
    

class VotingListView(GenericListView):
    table_name = "voting"
    sql = """
    WITH current_elections AS (
        SELECT * 
        FROM elections 
        WHERE Start_Date < GETDATE() AND GETDATE() < END_DATE
    ) (
    select U.Name, RT.Role_Name, COALESCE(COUNT(V.Vote_ID), 0) as Votes
    from voting V 
    right join candidates C on V.Candidate_ID = C.Candidate_ID
    right join users U on C.User_ID = U.User_ID
    join Role_Types RT on C.Role_ID = RT.Role_ID
    where C.Election_ID in (select election_id from current_elections)
    group by C.Candidate_ID, C.User_ID, RT.Role_Name, U.Name
    )
    """
    pk_field = "Vote_ID"

class VotingPageView(GenericPageView):
    table_name = "voting"
    search_field = "Vote_ID"
    fields = ["Voter_ID, Candidate_ID"]
    pk_field = "Vote_ID"
    redirect_to = "list_voting"
    form_class = Voting_form


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk", None)
        print("I've got pk", pk)
        context["object"] = self.get_object(pk) if pk else None
        context["fields"] = self.fields
        user_privilege = self.request.session.get("privilege", None)
        user_id = self.request.session.get("user_id", None)
        print("The user id is ", user_id)
        context["user_id"] = user_id
        context["has_privilege"] = user_privilege == 1  # Only show actions if privilege is 1

        obj = self.get_object(pk) if pk else None
        initial_data = {key: value for key, value in obj.items() if key != self.pk_field} if obj else None
        print(self.form_class)
        context["form"] = self.form_class(initial=initial_data) if obj else self.form_class(user_id = user_id)
        print("The form with context is ", context["form"].fields)
        return context




    def post(self, request, *args, **kwargs):
        user_id = self.request.session.get("user_id", None)
        form = self.form_class(request.POST, user_id = user_id)
        print(f"Current class: {self.__class__.__name__}")  # Debug the class name
        if form.is_valid(): #If valid do the thing
            data = form.cleaned_data
            print("I've got data", data)
            pk = self.kwargs.get("pk")
            with connection.cursor() as cursor:
                if pk: #in this case we are updating
                    set_clause = ", ".join([f"{field} = %s" for field in self.fields])
                    sql = f"update {self.table_name} set {set_clause} where {self.pk_field} = %s"
                    cursor.execute(sql, list(data.values()) + [pk])
                else:

                    sql = "BEGIN TRAN "
                    self.fields = self.fields[0].split(",")
                    columns = ", ".join(self.fields)
                    placeholders = ", ".join(["%s"] * len(self.fields))

                    biglist = []

                    for vote in data.items():
                        sql += f"insert into {self.table_name} ({columns}) values ({placeholders})"
                        print(str(user_id), vote[1])
                        print(sql)
                        biglist += [str(user_id)]
                        biglist += [vote[1]]

                    sql += " COMMIT"

                    print(biglist)


                    cursor.execute(sql, biglist)

            return redirect(self.redirect_to)
        return render(request, self.template_name, {'form' : form}) #Otherwise ask again
    
class VotingDeleteView(GenericDeleteView):
    table_name = "voting"
    pk_field = "Vote_ID"
    redirect_to = "list_voting"
