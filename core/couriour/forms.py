from django import forms
from django.contrib.auth.models import User

from core.models import customer

class profileform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name']
class customerForm(forms.ModelForm):
    
    class Meta:
        model = customer
        fields = ("avtar",)
        