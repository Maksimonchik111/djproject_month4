from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views import generic

from . import forms, models



class RegisterView(generic.FormView):
    template_name = 'register.html'
    form_class = forms.CustomRegisterForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AuthLoginView(LoginView):
    template_name = 'login.html'
    form_class = forms.CustomLoginForm

    def get_success_url(self):
        return '/resume_list/'

class AuthLogoutView(LogoutView):
    next_page = '/login/'


class ResumeListView(generic.ListView):
    template_name = 'resume_list.html'
    paginate_by = 2
    model = models.CustomUser
    context_object_name = 'resumes'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumes'] = context['page_obj']
        return context


class ResumeDetailView(generic.DetailView):
    template_name = 'resume_detail.html'
    model = models.CustomUser
    context_object_name = 'resume'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj


class SearchView(generic.ListView):
    template_name = 'resume_list.html'
    context_object_name = 'resumes'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.filter(username__icontains=self.request.GET.get('s'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context