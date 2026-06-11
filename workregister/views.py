from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import  AuthenticationForm
from . import models, forms
from django.core.paginator import Paginator
from django.db.models import F



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
    paginator = Paginator(resumes, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'resume_list.html', {'resumes': page_obj})


def resume_detail_view(request, id):
    if request.method == 'GET':
        resume = models.CustomUser.objects.get(id=id)

        viewed_blog = request.session.get('viewed_blog', [])

        if id not in viewed_blog:
            resume.views = F("views") + 1
            resume.save()
            resume.refresh_from_db()
            viewed_blog.append(id)
            request.session['viewed_blog'] = viewed_blog

        return render(request, 'resume_detail.html', context={'resume': resume})


def search_view(request):
    query = request.GET.get('s', '')
    if query:
        resumes = models.CustomUser.objects.filter(username__icontains=query)
    else:
        return HttpResponse('Блог не найден!')

    return render(request,
                  template_name='resume_list.html',
                  context={'resumes': resumes})