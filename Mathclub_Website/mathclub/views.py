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
    return redirect('Math_club:register_page') 


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

#TODO: Check for privs in creation and deletion
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
            #TODO: Select from fields here 
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
        context["has_privilege"] = user_privilege == 1  # Only show actions if privilege is 1

        obj = self.get_object(pk) if pk else None
        initial_data = {key: value for key, value in obj.items() if key != self.pk_field} if obj else None
        context["form"] = self.form_class(initial=initial_data) if obj else self.form_class()
        print(context)
        print(initial_data)
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



class GenericDeleteView(View):
    table_name = None
    pk_field = ""
    redirect_to = ""

    def post(self, request, pk):
        with connection.cursor() as cursor:
            sql = f"delete from {self.table_name} where {self.pk_field} = %s"
            cursor.execute(sql, [pk])
        return redirect(self.redirect_to)

# Elections
    
class ElectionsListView(GenericListView):
    table_name = "elections"
    sql = """
select Election_ID, Start_Date, End_Date from Elections 
"""
    pk_field = "Election_ID"


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

class Locations_DeleteView(GenericDeleteView):
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