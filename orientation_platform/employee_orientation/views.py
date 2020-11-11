from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def homepage(request):
    return render(request, template_name='homepage.html')


def about(request):
    return render(request, template_name='pages/about.html')


def login_user(request):
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.employee_role == 'TRAINEE':
                return redirect('trainee_profile')
            elif request.user.employee_role == 'MENTOR':
                return redirect('mentor_profile')
        else:
            return redirect('no_account_page')
    return render(request, template_name='registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('homepage')


def ask_for_registration(request):
    return render(request, template_name='pages/no_account_page.html')


@login_required()
def trainee_profile(request):
    return render(request, template_name='pages/trainee_profile.html')


@login_required()
def mentor_profile(request):
    return render(request, template_name='pages/mentor_profile.html')

@login_required()
def trainings(request):
    return render(request, template_name='pages/trainings.html')
