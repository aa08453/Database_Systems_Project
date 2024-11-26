from django.urls import path
from django.urls import reverse
from . import views
from .views import *

urlpatterns = [
    path('', views.login_page, name='login_page'),  # Serve at root
    path('register/',views.register_page, name='register_page'),
    path('teams',views.team_page, name='teams_page'),
    path ('finance',views.finance_page, name='finance_page'),
    path('finance/submit', views.finance_submit, name='finance_submit'),  # Add this line
    path('voting', views.voting_poll, name='voting_poll'),  # Add this line
    path('submit_blog', views.submit_blog, name='submit_blog'),  # Add this line
    path('additem', views.add_product_page, name='add_product'),  # Add this line
    path('main', views.main_page, name='main_page'),  # Add this line



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


    #Blogs
    path('Blogs/', Blogs_ListView.as_view(), name='list_blogs'),
    path('Blogs/create/', Blogs_PageView.as_view(), name='create_blogs'),
    path('Blogs/update/<int:pk>/', Blogs_PageView.as_view(), name='update_blogs'),
    # delete constraint 
    # need to delete from tables where it is referred to as FK
    path('Blogs/delete/<int:pk>/', Blogs_DeleteView.as_view(), name='delete_blogs'),


]

