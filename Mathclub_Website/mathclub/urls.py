from django.urls import path
from django.urls import reverse
from . import views


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
    path('election/create', views.election_create_page, name='election_create'),  # Add this line
    path('election/retrieve', views.election_retrieve_page, name='election_view'),  # Add this line
    path('election/update/<int:election_id>/', views.election_update_page, name='election_update'),  # Add this line
]

