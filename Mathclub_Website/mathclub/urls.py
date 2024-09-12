from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),  # Serve at root
    path('register',views.register_page, name='register_page'),
    path('teams',views.team_page, name='teams_page'),
]
