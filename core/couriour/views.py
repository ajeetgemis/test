
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login
from django.contrib import messages
from .forms import profileform,customerForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import stripe
from django.conf import settings
stripe.api_key=settings.STRIPE_API_SECRET_KEY





@login_required()
def couriour(request):

    return redirect(reverse('couriour:profile'))

@login_required(login_url='/sign_in/?next=/couriour/')
def profile_couriour(request):
    print(request.user)
    formobj=profileform(instance=request.user)
    password_form=PasswordChangeForm(request.user)
    if request.method=="POST":
        
        print( request.POST.get('action'))
        if request.POST.get('action')=='profile':
            formobj=profileform(request.POST,instance=request.user)
            
            if formobj.is_valid():
                formobj.save()
                
               
                return redirect(reverse('couriour:profile'))
        elif request.POST.get('action')=='customer':
            obj=customerForm(request.POST,instance=request.user.customer)
            if obj.is_valid():
                obj.save()
                print("customer updated")
                return redirect(reverse('couriour:profile'))
        elif request.POST.get('action')=='password':
            obj=PasswordChangeForm(request.user,request.POST)
            print("Change password called")
            print(obj)
            if obj.is_valid():
                user=obj.save()
                print("PRINTTTTTTTTTTTTTTTTTTTTT")
                update_session_auth_hash(request,user)
                return redirect(reverse('couriour:profile'))   
        print("post method called")
    

    
    print(formobj)
    cusobj=customerForm()
    
    return render (request,'profile.html',{'user_form':formobj,'cus_form':cusobj,'pass_form':password_form})


@login_required(login_url='/sign_in/?next=/couriour/')
def payment_method_page(request):
    print("customer",request.user.customer)
    current_customer=request.user.customer
    print( current_customer)
    if not current_customer.strip_customer_id:
        customer = stripe.Customer.create()
        current_customer.strip_customer_id=customer['id']
        current_customer.save()
    intent=stripe.SetupIntent.create(customer=current_customer.strip_customer_id)
    print(intent)
    print(intent['id'])
    print(intent['client_secret'])

    return render(request,'payment_method_page.html',{'client_secret':intent['client_secret'],'STRIPE_API_PUBLIC_KEY':settings.STRIPE_API_PUBLIC_KEY})
