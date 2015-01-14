from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class userform(forms.Form):
    email = forms.EmailField(label = 'Email')
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(render_value = False))
    
class Registerform(forms.Form):
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(render_value = False))
    password2 = forms.CharField(label = 'Verify Password', widget = forms.PasswordInput(render_value = False))
    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(username = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('that email is already registered')
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("passwords do not match")
        return password2
    