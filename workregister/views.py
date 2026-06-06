from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import  AuthenticationForm
from . import models, forms


def register_view(request):
    if request.method == 'POST':
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomRegisterForm()

    return render(request, 'register.html', {'form': form})


def auth_login_view(request):
    if request.method == 'POST':
        form = forms.CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/resume_list/')
    else:
        form = forms.CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def auth_logout_view(request):
    logout(request)
    return redirect('/login/')


def resume_list_view(request):
    resumes = models.CustomUser.objects.all().order_by('-id')

    return render(request, 'resume_list.html', {'resumes': resumes})