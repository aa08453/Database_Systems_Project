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

class Form_Custom(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check_for_duplicate_combination(self, **kwargs):
        table_name = kwargs.get('table_name')
        
        if not table_name:
            raise ValueError("Table name must be provided in kwargs")


        where_clause = " AND ".join([f"{field} = %s" for field in kwargs if field != 'table_name'])
        values = [value for key, value in kwargs.items() if key != 'table_name']

        check_sql = f"""
        SELECT COUNT(1)
        FROM {table_name}
        WHERE {where_clause}
        """
        print(check_sql)
        print(values)

        
        with connection.cursor() as cursor:
            cursor.execute(check_sql, values)
            count = cursor.fetchone()[0]
            
            if count > 0:
                # If the combination already exists, add an error to the form for each field involved
                for field in kwargs:
                    if field != 'table_name':  # Avoid adding error for 'table_name'
                        self.add_error(field, f"This combination of {field} already exists.")

class candidates_form(Form_Custom):

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
    
class Majors_form(Form_Custom):
    Name = forms.CharField(
        widget=forms.TextInput()
    )   

    def clean(self):
        cleaned_data = super().clean()
        self.check_for_duplicate_combination(table_name = "Majors", Name = cleaned_data.get("Name"))


    
class Tags_form(forms.Form):
    tag = forms.CharField(
        widget=forms.TextInput()
    )  

    def clean(self):
        data = self.cleaned_data  # Use self.cleaned_data, not form.cleaned_data
        # Check if the 'major' already exists in the database
        with connection.cursor() as cursor:
            # Assuming you're checking for a unique field (like 'major')
            check_sql = f"SELECT COUNT(1) FROM Majors WHERE Name = %s"
            cursor.execute(check_sql, [data["major"]])  # 'major' should match the field name
            count = cursor.fetchone()[0]
            print("Got here")
            if count > 0:
                # Add error to the 'major' field
                self.add_error('major', 'This value already exists.')  # Correct way to add errors
                # Optionally, you can raise a ValidationError here, but adding the error is sufficient
                return data  # You can return the cleaned data, even if errors were added
        return data
