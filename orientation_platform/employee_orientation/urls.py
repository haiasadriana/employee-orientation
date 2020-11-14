from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('trainee/', views.trainee_profile, name='trainee_profile'),
    path('mentor/', views.mentor_profile, name='mentor_profile'),
    path('no_account_page/', views.ask_for_registration, name='no_account_page'),
    path('trainings/', views.trainings, name='trainings'),
    path('add_training/', views.add_training, name='add_training'),
    path('add_training_material/', views.add_training_material, name='add_training_material'),
]
