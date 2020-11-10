from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('trainee/', views.trainee_profile, name='trainee_profile'),
    path('mentor/', views.mentor_profile, name='mentor_profile'),
    path('no_account_page/', views.ask_for_registration, name='no_account_page'),
]
