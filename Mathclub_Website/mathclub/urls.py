from django.urls import path
from django.urls import reverse
from . import views
from .views import *

urlpatterns = [
    path('', views.login_page, name='login_page'),  # Serve at root
    path('register/',views.register, name='register_page'),
    path('member_registration_page', Members.as_view(), name='member_registration_page'),
    path('outsider_registartion_page', Outsiders.as_view(), name='outsider_registration_page'),
    path('admin_registartion_page', Admins.as_view(), name='admin_registration_page'),
    

    path('voting', views.voting_poll, name='voting_poll'),  # Add this line
    # path('submit_blog', views.submit_blog, name='submit_blog'),  # Add this line
    path('additem', views.add_product_page, name='add_product'),  # Add this line
    path('main', views.main_page, name='main_page'),  # Add this line

    
    path('Roles/create/', Team_Roles.as_view(), name='create_Roles'),
    path('Roles/',List_Roles.as_view(),name="list_Roles"),# Add this line
    path('Team_Roles/update/<int:pk>/', Team_Roles.as_view(), name='update_Roles'),  # Add this line
    path('Team_Roles/delete/<int:pk>/', Team_Roles_DeleteView.as_view(), name='delete_Roles'),  # Add this line
    
    

    path('Teams/',Teams_ListView.as_view(), name='list_Teams'),    
    path('Teams/create/',Teams.as_view(), name='create_Teams'),
    path('Teams/update/<int:pk>/',Teams.as_view(), name='update_Teams'),
    path('Teams/delete/<int:pk>/',Teams_DeleteView.as_view(), name='delete_Teams'),
    





    path ('Finances/',Finance_ListView.as_view(), name='list_Finance'),
    path('Finances/create/', Finance_PageView.as_view(), name='create_Finance'),  # Add this line
    path('Finances/delete/<int:pk>/', Finance_DeleteView.as_view(), name='delete_Finance'),
    path('Finances/update/<int:pk>/', Finance_PageView.as_view(), name='update_Finance'),  # Add this line



    #elections. We delete through the update.
    # path('election/create', views.election_create_page, name='election_create'),  # Add this line
    # path('election/retrieve', views.election_retrieve_page, name='election_view'),  # Add this line
    # path('election/update/<int:election_id>/', views.election_update_page, name='election_update'),  # Add this line


    # path('election', views.election_test, name='test')
    path('elections/', ElectionsListView.as_view(), name='list_elections'),
    path('elections/create/', ElectionsPageView.as_view(), name='create_election'),
    path('elections/update/<int:pk>/', ElectionsPageView.as_view(), name='update_election'),
    path('elections/delete/<int:pk>/', ElectionsDeleteView.as_view(), name='delete_election'),


    #Candidates
    path('candidates/', CandidatesListView.as_view(), name='list_candidates'),
    path('candidates/create/', CandidatesPageView.as_view(), name='create_candidate'),
    path('candidates/update/<int:pk>/', CandidatesPageView.as_view(), name='update_candidate'),
    path('candidates/delete/<int:pk>/', CandidatesDeleteView.as_view(), name='delete_candidate'),



    #Roles
    path('Role_Types/', Role_TypesListView.as_view(), name='list_Role_Types'),
    path('Role_Types/create/', Role_TypesPageView.as_view(), name='create_Role_Type'),
    path('Role_Types/update/<int:pk>/', Role_TypesPageView.as_view(), name='update_Role_Type'),
    path('Role_Types/delete/<int:pk>/', Role_TypesDeleteView.as_view(), name='delete_Role_Type'),
    
    #Locations
    path('Locations/', Locations_ListView.as_view(), name='list_locations'),
    path('Locations/create/', Locations_PageView.as_view(), name='create_locations'),
    path('Locations/update/<int:pk>/', Locations_PageView.as_view(), name='update_locations'),
    # delete constraint 
    # need to delete from tables where it is referred to as FK
    path('Locations/delete/<int:pk>/', Locations_DeleteView.as_view(), name='delete_locations'),
    
    #Majors
    path('Majors/', Majors_ListView.as_view(), name='list_majors'),
    path('Majors/create/', Majors_PageView.as_view(), name='create_majors'),
    path('Majors/update/<int:pk>/', Majors_PageView.as_view(), name='update_majors'),
    # delete constraint 
    # need to delete from tables where it is referred to as FK
    path('Majors/delete/<int:pk>/', Majors_DeleteView.as_view(), name='delete_majors'),
    
    #Tags
    path('Tags/', Tags_ListView.as_view(), name='list_tags'),
    path('Tags/create/', Tags_PageView.as_view(), name='create_tags'),
    path('Tags/update/<int:pk>/', Tags_PageView.as_view(), name='update_tags'),
    # delete constraint 
    # need to delete from tables where it is referred to as FK
    path('Tags/delete/<int:pk>/', Tags_DeleteView.as_view(), name='delete_tags'),
    
    #Products
    path('Products/', Products_ListView.as_view(), name='list_products'),
    path('Products/create/', Products_PageView.as_view(), name='create_products'),
    path('Products/update/<int:pk>/', Products_PageView.as_view(), name='update_products'),
    # delete constraint 
    # need to delete from tables where it is referred to as FK
    path('Products/delete/<int:pk>/', Products_DeleteView.as_view(), name='delete_products'),
    
    #Events
    path('Events/', Events_ListView.as_view(), name='list_events'),
    path('Events/create/', Events_PageView.as_view(), name='create_events'),
    path('Events/update/<int:pk>/', Events_PageView.as_view(), name='update_events'),
    # delete constraint 
    # need to delete from tables where it is referred to as FK
    path('Events/delete/<int:pk>/', Events_DeleteView.as_view(), name='delete_events'),
    
    #Club_Items
    path('Club_Items/', Club_Items_ListView.as_view(), name='list_club_Items'),
    path('Club_Items/create/', Club_Items_PageView.as_view(), name='create_club_Items'),
    path('Club_Items/update/<int:pk>/', Club_Items_PageView.as_view(), name='update_club_Items'),
    path('Club_Items/delete/<int:pk>/', Club_Items_DeleteView.as_view(), name='delete_club_Items'),


    #Blogs
    path('Blogs/', Blogs_ListView.as_view(), name='list_blogs'),
    path('Blogs/create/', Blogs_PageView.as_view(), name='create_blogs'),
    path('Blogs/update/<int:pk>/', Blogs_PageView.as_view(), name='update_blogs'),
    # delete constraint 
    # need to delete from tables where it is referred to as FK
    path('Blogs/delete/<int:pk>/', Blogs_DeleteView.as_view(), name='delete_blogs'),


]

