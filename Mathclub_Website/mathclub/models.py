# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AttendeeType(models.Model):
    type_id = models.AutoField(primary_key=True)
    attendee_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'attendee_type'


class Attendee(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, db_column='event_id')
    type = models.ForeignKey(AttendeeType, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'attendees'
        unique_together = (('user', 'event'),)
    # Making user_event pair unique with user being the primary key


class Blog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog'


class BlogContent(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, db_column='post_id')
    file = models.IntegerField()
    file_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'blog_content'


class BlogTag(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, db_column='post_id')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, db_column='tag_id')

    class Meta:
        db_table = 'blog_tags'
        unique_together = (('post', 'tag'),)


class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    role = models.ForeignKey('RoleType', on_delete=models.CASCADE)
    election = models.ForeignKey('Election', on_delete=models.CASCADE)

    class Meta:
        db_table = 'candidates'
        unique_together = (('user', 'role', 'election'),)
    # Making user_role_election composite unique with candidate_id as primary key


class ClubItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)

    class Meta:
        db_table = 'club_items'


class Election(models.Model):
    election_id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = 'election'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    scale = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'event'


class EventLeader(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    event_lead = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'event_leaders'
        unique_together = (('event', 'event_lead'),)
    # Making the event_lead unique together with event by making event_lead primary key


class Inventory(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='product_id')
    quantity_in_stock = models.IntegerField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    class Meta:
        db_table = 'inventory'
        unique_together = (('product', 'location'),)
    # Making product_location unique with product as the primary key


class Leadership(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    role = models.ForeignKey('RoleType', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = 'leadership'
        unique_together = (('user', 'role', 'start_date'),)
    # Making user_role_start_date composite unique with user as the primary key


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'locations'


class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'majors'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('User', on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_date = models.DateField()

    class Meta:
        db_table = 'orders'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'order_details'
        unique_together = (('order', 'product'),)
    # Making order_product unique with order as the primary key


class Privilege(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='privileges')
    start_date = models.DateField()
    privilege = models.CharField(max_length=255)
    end_date = models.DateField()

    class Meta:
        db_table = 'privileges'
        unique_together = (('user', 'start_date'),)
    # Making user_start_date unique with user as the primary key


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'


class RoleType(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'role_types'


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField()

    class Meta:
        db_table = 'sales'
        unique_together = (('product', 'sale_date'),)
    # Making product_sale_date unique with product as the primary key


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tags'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255)
    team_lead = models.ForeignKey('User', on_delete=models.CASCADE)
    date_created = models.DateTimeField()

    class Meta:
        db_table = 'team'


class TeamMember(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey('TeamRole', on_delete=models.SET_NULL, null=True)
    date_started = models.DateField()
    date_ended = models.DateField(null=True, blank=True)
    is_leader = models.BooleanField()

    class Meta:
        db_table = 'team_members'
        unique_together = (('user', 'team'),)
    # Making user_team unique with user as the primary key


class TeamRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    role_description = models.TextField()

    class Meta:
        db_table = 'team_roles'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    reg_date = models.DateTimeField()
    contact_number = models.CharField(max_length=15)
    privilege = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    cnic = models.CharField(max_length=13, null=True, blank=True)

    class Meta:
        db_table = 'user'
