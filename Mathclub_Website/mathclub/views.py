from django.shortcuts import render, redirect
from .front import *
from django.contrib import messages
from datetime import datetime
from .myutils import *

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, FormView, DeleteView, View
from django.urls import reverse_lazy

from .forms import election_form, candidates_form
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
    table_name = None
    pretty_print = None
    search_field = "" #We can override this later
    fields = []
    pk_field = ""

    #TODO: Make a insertion check hook

    def get_queryset(self, query=""):
        with connection.cursor() as cursor:
            if self.pretty_print is None:
                fields = ", ".join(self.fields)
                sql = f"select {fields} from {self.table_name} "
                if query:
                    sql += f"where {self.search_field} like %s"
                    cursor.execute(sql, [f"%{query}%"])
                else:
                    cursor.execute(sql)
            else:
                if query:
                    sql = self.pretty_print + f"where {self.search_field} like %s"
                    cursor.execute(sql, [f"%{query}%"])
                else:
                    cursor.execute(self.pretty_print)

            columns = [col[0] for col in cursor.description]
            for x in range(0, len(columns)):
                if columns[x] == self.pk_field:
                    columns[x] = "pk_field"


            return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")
        context["items"] = self.get_queryset(query)
        context["table_name"] = self.table_name
        context["create_url"] = f"/{self.table_name}/create/"
        context["update_url"] = f"/{self.table_name}/update/"
        context["delete_url"] = f"/{self.table_name}/delete/"
        user_privilege = self.request.session.get("privilege", None)
        print(user_privilege)
        context["has_privilege"] = user_privilege == 1  # Only show actions if privilege is 1
        print(context)
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
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

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
                    print(sql)
                    print(data.values())
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


    
class ElectionsListView(GenericListView):
    table_name = "elections"
    search_field = "start_date" #We can override this later
    fields = ["start_date", "end_date"]
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


class CandidatesListView(GenericListView):
    table_name = "candidates"
    search_field = "Candidate_ID"
    fields = ["Candidate_ID", "Role_ID", "Election_ID", "User_ID"]
    pretty_print = """
select Candidate_ID, R.Role_Name, E.Start_Date, U.Name
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

