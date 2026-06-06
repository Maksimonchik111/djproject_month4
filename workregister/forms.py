from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class CustomRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, initial='+996')
    email = forms.EmailField(required=True)
    gender = forms.CharField(max_length=25, required=True, initial='m')
    link_to_resume = forms.URLField(required=True)
    position = forms.CharField(max_length=150)
    experience_years = forms.IntegerField(required=True)
    captcha = CaptchaField(label='Введите код с картинки')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'gender',
            'link_to_resume',
            'position',
            'experience_years'
        )

    def save(self, commit = True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.phone_number = self.cleaned_data['phone_number']
        user.gender = self.cleaned_data['gender']
        user.link_to_resume = self.cleaned_data['link_to_resume']
        user.position = self.cleaned_data['position']
        user.experience_years = self.cleaned_data['experience_years']
        if commit:
            user.save()
        return user


class CustomLoginForm(AuthenticationForm):
    captcha = CaptchaField(label='Подтвердите, что вы не робот')