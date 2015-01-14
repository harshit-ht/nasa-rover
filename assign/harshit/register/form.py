from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def loginform(forms.Form):
    email = forms.EmailField(label = 'Email')
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(render_value = False))
    
def registerform(forms.Form):
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(render_value = False))
    password2 = forms.CharField(label = 'Verify Password', widget = forms.PasswordInput(render_value = False))
    mobileno = forms.BigIntegerField()
    
