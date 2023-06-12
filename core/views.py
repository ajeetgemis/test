from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.
def base(request):
    return render (request,'main.html')


def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        obj=authenticate(username=username,password=password)
        if obj:
            login(request,obj)
            print("login called")
            return render(request,'profile.html')


def sign_up(request):
    fom=forms.signupform()
    if request.method=="POST":
        data=forms.signupform(request.POST)
        print("data")
        if data.is_valid():
            email=data.cleaned_data.get('email').lower()
            print(email)
            form=data.save(commit=False)
            form.username=email
            form.save()
            messages.success(request,'User Creation Successfully')
            #login(request,form)
           # return redirect('/')
            return render(request,'sign_up.html',{'form':fom})
        print("POST METHOD")
 
    return render(request,'sign_up.html',{'form':fom})
def test(request):
    form=forms.signupform()
    return render(request,'test.html',{'form':form})