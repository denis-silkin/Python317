from django.shortcuts import render, redirect
from .models import Skills
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def sign_up_user(request):
    if request.method == 'GET':
        return render(request, 'skills/sign_up_user.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')

            except IntegrityError:
                return render(request, 'skills/sign_up_user.html', {'form': UserCreationForm(),
                                                                    'error': 'Такое имя пользователя уже существует.'
                                                                             ' Задайте другое!!!'})
        else:
            return render(request, 'skills/sign_up_user.html', {'form': UserCreationForm(),
                                                                'error': 'Пароли не совпадают!!!'})


def current(request):
    return render(request, 'skills/current.html')


def index(requests):
    project_serial = Skills.objects.all()
    return render(requests, 'skills/index.html', {'project_serial': project_serial})


def log_in_user(request):
    if request.method == 'GET':
        return render(request, 'skills/log_in_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'skills/log_in_user.html', {'form': AuthenticationForm(), 'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('index')


def log_out_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
