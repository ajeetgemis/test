from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class signupform(UserCreationForm):
    email=forms.EmailField(max_length=100)
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)


    class Meta:
        model=User
        fields=('email','first_name','last_name','password1','password2')
