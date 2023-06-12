from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.contrib import messages
# Create your views here.



@login_required
def customer(request):
    return render (request,'customer.html')
