# forms.py
from django import forms
from django.db import connection

class BlogForm(forms.Form):
    author = forms.CharField(label="Author Name", max_length=100)
    title = forms.CharField(label="Title", max_length=255)
    content = forms.CharField(label="Blog Content", widget=forms.Textarea)

class election_form(forms.Form):
    Start_Date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))
    End_Date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))

class DynamicChoiceField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        self.query = kwargs.pop('query', None)
        self.argument_string = kwargs.pop('argument_string', '') #TODO: see if this is right
        super().__init__(*args, **kwargs)
        self.choices = self.prepare_choices()

    def prepare_choices(self):
        if self.query:
            with connection.cursor() as cursor:
                cursor.execute(self.query, self.argument_string) 
                rows = cursor.fetchall()

            result = [(row[0], row[1]) for row in rows]
            print(result)
            return result
        return []


class candidates_form(forms.Form):

    role = DynamicChoiceField(
        query = """
        select Role_ID, Role_Name
        from Role_Types
        """
    )

    elections = DynamicChoiceField(
        query = """
        select Election_ID, Start_Date
        from Elections
        """
    )

    nominee = DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """
    )

class Role_Types_form(forms.Form):
    role = forms.CharField(
        widget=forms.TextInput()
    )

class Locations_form(forms.Form):
    location = forms.CharField(
        widget=forms.TextInput()
    )
    
class Majors_form(forms.Form):
    major = forms.CharField(
        widget=forms.TextInput()
    )   
    
class Tags_form(forms.Form):
    tag = forms.CharField(
        widget=forms.TextInput()
    )  

class Blogs_form(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput()
    )
    date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))
    content = forms.CharField(
        widget=forms.TextInput()
    )
    author =  DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """
    )
    tag = DynamicChoiceField(
        query = """
        select Tag_ID, Tag_Name
        from Tags
        """
    )
