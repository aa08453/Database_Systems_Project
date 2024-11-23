# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AttendeeTypes(models.Model):
    type_id = models.AutoField(primary_key=True)
    attendee_type = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Attendee_Types'


class BlogContents(models.Model):
    post_id = models.AutoField(db_column='Post_ID', primary_key=True)  # Field name made lowercase.
    file_path = models.CharField(db_column='File_Path', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    file_type = models.CharField(db_column='File_Type', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Blog_Contents'


class Blogs(models.Model):
    post_id = models.AutoField(db_column='Post_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='Date_Created')  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Blogs'


class ClubItems(models.Model):
    item_id = models.AutoField(db_column='Item_ID', primary_key=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='Item_Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    storage = models.CharField(db_column='Storage', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Club_Items'


class Elections(models.Model):
    election_id = models.AutoField(db_column='Election_ID', primary_key=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_Date')  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Elections'


class EventLeaders(models.Model):
    event = models.OneToOneField('Events', models.DO_NOTHING, db_column='Event_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Event_ID, Event_Lead) found, that is not supported. The first column is selected.
    event_lead = models.ForeignKey('Users', models.DO_NOTHING, db_column='Event_Lead')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Event_Leaders'
        unique_together = (('event', 'event_lead'),)


class EventParticipations(models.Model):
    event = models.OneToOneField('Events', models.DO_NOTHING, db_column='Event_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Event_ID, Attendee) found, that is not supported. The first column is selected.
    attendee = models.ForeignKey('Users', models.DO_NOTHING, db_column='Attendee')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Event_Participations'
        unique_together = (('event', 'attendee'),)


class EventTeams(models.Model):
    event_id = models.IntegerField(db_column='Event_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Event_ID, Team_ID) found, that is not supported. The first column is selected.
    team_id = models.IntegerField(db_column='Team_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Event_Teams'
        unique_together = (('event_id', 'team_id'),)


class Events(models.Model):
    event_id = models.AutoField(db_column='Event_ID', primary_key=True)  # Field name made lowercase.
    event_name = models.CharField(db_column='Event_Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_Date')  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_Date')  # Field name made lowercase.
    location = models.IntegerField(db_column='Location')  # Field name made lowercase.
    scale = models.IntegerField(db_column='Scale')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'


class Locations(models.Model):
    location_id = models.AutoField(db_column='Location_ID', primary_key=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Locations'


class Majors(models.Model):
    major_id = models.AutoField(db_column='Major_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Majors'


class OrderDetails(models.Model):
    order_id = models.AutoField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='Product_ID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order_Details'


class Products(models.Model):
    product_id = models.AutoField(db_column='Product_ID', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products'


class Responsibilities(models.Model):
    item_id = models.AutoField(db_column='Item_ID', primary_key=True)  # Field name made lowercase.
    person_responsible = models.IntegerField(db_column='Person_Responsible')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responsibilities'


class RoleTypes(models.Model):
    role_id = models.AutoField(db_column='Role_Id', primary_key=True)  # Field name made lowercase.
    role_name = models.CharField(db_column='Role_Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Role_Types'


class Sessions(models.Model):
    session_key = models.CharField(db_column='SESSION_KEY', primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sessions'


class Tags(models.Model):
    tag_id = models.AutoField(db_column='Tag_ID', primary_key=True)  # Field name made lowercase.
    tag_name = models.CharField(db_column='Tag_Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tags'


class TeamRoles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    role_description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Team_Roles'


class Transactiontypes(models.Model):
    type_id = models.AutoField(db_column='Type_ID', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='Type_Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionTypes'


class UserMajors(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase. The composite primary key (User_ID, Major_ID, StartDate) found, that is not supported. The first column is selected.
    major = models.ForeignKey(Majors, models.DO_NOTHING, db_column='Major_ID')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User_Majors'
        unique_together = (('user', 'major', 'startdate'),)


class Users(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.
    contact_number = models.CharField(db_column='Contact_Number', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    privilege = models.IntegerField(db_column='Privilege')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnic = models.CharField(db_column='CNIC', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    huid = models.IntegerField(db_column='HUID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
