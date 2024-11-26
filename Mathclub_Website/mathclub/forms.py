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
    
from django import forms

class Major_choice(forms.Form):
    privilege = 0

    major = DynamicChoiceField(
        query="""
        select Major_ID, Name
        from Majors
        """
    )
    name = forms.CharField(widget=forms.TextInput())
    Contact_Number = forms.CharField(widget=forms.TextInput())
    Reg_Date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    password = forms.CharField(widget=forms.PasswordInput())
    HUID = forms.CharField(widget=forms.TextInput())
    
    

    def clean(self):
        """
        Set privilege based on the selected role and exclude role from final data.
        """
        cleaned_data = super().clean()
        role = cleaned_data.get("role")

        # Map roles to privileges
        privilege_map = {
            "admin": 1,
            "member": 0,
            "outsider": -1,
        }

        # Dynamically set privilege based on role
        cleaned_data["privilege"] = privilege_map.get(role, -1)

        # Remove role from cleaned data (if needed)
        if "role" in cleaned_data:
            del cleaned_data["role"]

        return cleaned_data

class Outsider(forms.Form):
    privilege = -1

    
    name = forms.CharField(widget=forms.TextInput())
    Contact_Number = forms.CharField(widget=forms.TextInput())
    Reg_Date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    CNIC = forms.CharField(widget=forms.TextInput())
    Address = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    

    def clean(self):
        """
        Set privilege based on the selected role and exclude role from final data.
        """
        cleaned_data = super().clean()
        role = cleaned_data.get("role")

        # Map roles to privileges
        privilege_map = {
            "admin": 1,
            "member": 0,
            "outsider": -1,
        }

        # Dynamically set privilege based on role
        cleaned_data["privilege"] = privilege_map.get(role, -1)

        # Remove role from cleaned data (if needed)
        if "role" in cleaned_data:
            del cleaned_data["role"]

        return cleaned_data


class Admins(forms.Form):
    privilege = 1

    major = DynamicChoiceField(
        query="""
        select Major_ID, Name
        from Majors
        """
    )
    name = forms.CharField(widget=forms.TextInput())
    Contact_Number = forms.CharField(widget=forms.TextInput())
    Reg_Date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    password = forms.CharField(widget=forms.PasswordInput())
    HUID = forms.CharField(widget=forms.TextInput())
    
    

    def clean(self):
        """
        Set privilege based on the selected role and exclude role from final data.
        """
        cleaned_data = super().clean()
        role = cleaned_data.get("role")

        # Map roles to privileges
        privilege_map = {
            "admin": 1,
            "member": 0,
            "outsider": -1,
        }

        # Dynamically set privilege based on role
        cleaned_data["privilege"] = privilege_map.get(role, -1)

        # Remove role from cleaned data (if needed)
        if "role" in cleaned_data:
            del cleaned_data["role"]

        return cleaned_data 