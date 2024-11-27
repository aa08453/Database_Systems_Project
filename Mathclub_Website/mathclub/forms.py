# forms.py
from django import forms
from django.db import connection

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

        
        with connection.cursor() as cursor:
            cursor.execute(check_sql, values)
            count = cursor.fetchone()[0]
            
            if count > 1:
                # If the combination already exists, add an error to the form for each field involved
                for field in kwargs:
                    if field != 'table_name':  # Avoid adding error for 'table_name'
                        self.add_error(field, f"This combination of {field} already exists.")




class BlogForm(Form_Custom):
    author = forms.CharField(label="Author Name", max_length=100)
    title = forms.CharField(label="Title", max_length=255)
    content = forms.CharField(label="Blog Content", widget=forms.Textarea)




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
            result.insert(0, (None, "Select an option"))
            return result
        return []



class election_form(Form_Custom):
    Start_Date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))
    End_Date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("Start_Date")
        end_date = cleaned_data.get("End_Date")
        with connection.cursor() as cursor:
            cursor.execute(
                    """
                        SELECT * 
                        FROM elections 
                        WHERE Start_Date < GETDATE() AND GETDATE() < END_DATE
                    """)
            active_elections = cursor.fetchall()

        if len(active_elections) > 0:
            self.add_error(None, f"An active election is already occurring")

        if start_date > end_date:
            self.add_error(None, f"Please use a valid timespan")

        return cleaned_data



class candidates_form(Form_Custom):

    role = DynamicChoiceField(
        query = """
        select Role_ID, Role_Name
        from Role_Types
        """, required = True
    )

    elections = DynamicChoiceField(
        query = """
            select Election_ID, CONVERT(VARCHAR, Start_Date, 120) + ' to ' + CONVERT(VARCHAR, End_Date, 120)
            FROM Elections;
        """, required = True
    )

    nominee = DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """, required = True
    )

    def clean(self):
        cleaned_data = super().clean()
        self.check_for_duplicate_combination(table_name = "candidates", 
                                             role_id = cleaned_data.get("Role_ID"),
                                             election_id = cleaned_data.get("Election_ID"),
                                             user_id = cleaned_data.get("User_ID"))



    #TODO: check for dupes

class Role_Types_form(Form_Custom):
    Role_Name = forms.CharField(
        widget=forms.TextInput(),
        required = True
    )

    def clean(self):
        cleaned_data = super().clean()
        self.check_for_duplicate_combination(table_name = "Role_Types", 
                                             Role_Name = cleaned_data.get("Role_Name"))





class Locations_form(Form_Custom):
    location_name = forms.CharField(
        widget=forms.TextInput(),
        required = True
    )
    def clean(self):
        cleaned_data = super().clean()
        self.check_for_duplicate_combination(table_name = "Locations", 
                                             location_name = cleaned_data.get("location_name"))
    
class Majors_form(Form_Custom):
    Name = forms.CharField(
        widget=forms.TextInput(),
        required = True
    )   

    def clean(self):
        cleaned_data = super().clean()
        self.check_for_duplicate_combination(table_name = "Majors", Name =
                                             cleaned_data.get("Name"))

    
class Tags_form(Form_Custom):
    Tag_Name = forms.CharField(
        widget=forms.TextInput(),
        required = True
    )  
    
class Products_form(Form_Custom):
    Product_Name = forms.CharField(
        label="Product Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product name'
        })
    )
    price = forms.IntegerField(
        label="Price",
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product price'
        })
    )
    stock = forms.IntegerField(
        label="Stock",
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter stock quantity'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        self.check_for_duplicate_combination(table_name = "Products", Product_Name =
                                             cleaned_data.get("Product_Name"))

class Events_form(forms.Form):
    
    lead = DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """
    )
    event = forms.CharField(
        widget = forms.TextInput()
    )
    start_date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))
    end_date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))
    location = DynamicChoiceField(
        query = """
        select Location_ID, Location_Name
        from Locations
        """
    )

    scale = forms.CharField(
        widget=forms.TextInput()
    )  
    
    description = forms.CharField(
        widget = forms.TextInput()
    )
    
class Club_Items_form(forms.Form):
    item = forms.CharField(
        widget = forms.TextInput()
    )
    
    storage = DynamicChoiceField(
        query = """
        select Location_ID, Location_Name
        from Locations
        """
    )
    
class Transaction_Types_form(forms.Form):
    transaction = forms.CharField(
        widget = forms.TextInput()
    )


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
        cleaned_data["privilege"] = privilege_map.get(role, 0)

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
        cleaned_data["privilege"] = privilege_map.get(role, 1)

        # Remove role from cleaned data (if needed)
        if "role" in cleaned_data:
            del cleaned_data["role"]

        return cleaned_data 


class teams(forms.Form):
    team_name = forms.CharField(widget=forms.TextInput())
    team_lead = DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """
    )
    creation_date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
    )

class Finances(forms.Form):
    Responsible = DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """
    )
    USER_ID = DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """
    )
    Transaction_type = DynamicChoiceField(
        query = """
        select Type_ID, Type_Name
        from Transaction_Types
        """
    )
    date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    description = forms.CharField(widget=forms.TextInput())    
    amount = forms.FloatField()
    
    
    
class Team_Roles_form(forms.Form):
    Role_Name = forms.CharField(widget=forms.TextInput())
    Role_Description = forms.CharField(widget=forms.TextInput())

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

def clean(self):
    data = self.cleaned_data  # Use self.cleaned_data, not form.cleaned_data
    # Check if the 'major' already exists in the database
    with connection.cursor() as cursor:
        # Assuming you're checking for a unique field (like 'major')
        check_sql = f"SELECT COUNT(1) FROM Majors WHERE Name = %s"
        cursor.execute(check_sql, [data["major"]])  # 'major' should match the field name
        count = cursor.fetchone()[0]
        if count > 0:
            # Add error to the 'major' field
            self.add_error('major', 'This value already exists.')  # Correct way to add errors
            # Optionally, you can raise a ValidationError here, but adding the error is sufficient
            return data  # You can return the cleaned data, even if errors were added
    return data


class Voting_form(Form_Custom):
    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)  
        with connection.cursor() as cursor:
            cursor.execute(
                    """
                        WITH current_elections AS (
                            SELECT * 
                            FROM elections 
                            WHERE Start_Date < GETDATE() AND GETDATE() < END_DATE
                        )(
                            SELECT R.Role_ID, R.Role_Name, CE.Start_Date,
                            CE.End_Date
                            FROM current_elections CE 
                            join candidates C on CE.Election_ID = C.Election_ID 
                            join Role_Types R on C.Role_ID = R.Role_ID
                            WHERE R.Role_ID is not NULL
                        )
                    """
                ) 
            roles = cursor.fetchall()

        if roles:
            for role in roles:
                self.fields[f"{role[1]} (For election from {role[2]} to {role[3]})"] = DynamicChoiceField(
                                                query = f"""
                                                WITH current_elections AS (
                                                    SELECT * 
                                                    FROM elections 
                                                    WHERE Start_Date < GETDATE() AND GETDATE() < END_DATE
                                                )
                                                (
                                                    SELECT C.Candidate_ID, U.Name
                                                    FROM current_elections CE 
                                                    join candidates C on CE.Election_ID = C.Election_ID
                                                    join users U on C.User_ID = U.User_ID
                                                    join Role_Types R on C.Role_ID = R.Role_ID
                                                    WHERE C.Role_ID = {role[0]} 
                                                )
                                                """
                                            )




class OrderDetails_form(forms.Form):
    orders =  DynamicChoiceField(
        query = """
        select Order_ID, Customer_ID
        from Orders
        """
    )
    products = DynamicChoiceField(
        query = """
        select Product_ID, Product_Name
        from Products
        """
    )
    
    quantity = forms.IntegerField()

#Orders FORM
class Orders_form(forms.Form):
    customer =  DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """
    )
    order_date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))
    
    delivery_date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))
class Leadership_form(forms.Form):
    user =  DynamicChoiceField(
        query = """
        select User_ID, Name
        from Users
        """
    )
    role = DynamicChoiceField(
        query = """
        select Role_ID, Role_Name
        from Role_Types
        """
    )
    Start_Date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))
    End_Date = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type':
                                                      'datetime-local'}))