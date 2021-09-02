from django import forms
from django.forms import PasswordInput


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='First name',
                                 error_messages={'required': 'Please enter your name'})
    last_name = forms.CharField(max_length=50, label='Last name',
                                error_messages={'required': 'Please enter your last name'})
    email = forms.CharField(max_length=50, label='Email', error_messages={'required': 'Please enter email'})
    username = forms.CharField(max_length=50, label='Username',
                               error_messages={'required': 'Please enter your username'})
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': PasswordInput(),
    }

    image = forms.ImageField()


RegisterForm = RegisterForm


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, label='Email',
                            error_messages={'required': 'Please enter your email'})
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': PasswordInput(),
    }


LoginForm = LoginForm
