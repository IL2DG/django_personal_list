from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Workers


@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='login')
def list_work(request):
    workers = Workers.objects.all()
    context = {
        'lw': workers
    }
    return render(request, 'main/list.html', context)


def login_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Неверный логин или пароль.')
    context = {}
    return render(request, 'main/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')






