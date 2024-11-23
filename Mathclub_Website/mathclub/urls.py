from django.urls import path
from . import views

app_name = 'Math_club'  # Add this line


urlpatterns = [
    path('', views.login_page, name='login_page'),  # Serve at root
    path('register/',views.register_page, name='register_page'),
    path('teams/',views.team_page, name='teams_page'),
    path ('finance',views.finance_page, name='finance_page'),
    path('finance/submit', views.finance_submit, name='finance_submit'),  # Add this line
    path('voting', views.voting_poll, name='voting_poll'),  # Add this line
    path('submit_blog', views.submit_blog, name='submit_blog'),  # Add this line
    path('additem', views.add_product_page, name='add_product'),  # Add this line
    path('main', views.main_page, name='main_page'),  # Add this line
    path('logout/',views.logout_view, name='logout'),
]
