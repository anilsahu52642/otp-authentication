from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import *
from random import *
from twilio.rest import Client
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# for sending otp...........
def sendotp(phone):
    OTPcode = randint(10000, 99999)
    phonenumber = phone
    account_sid = 'AC3b8194f2a430b820730b954f5983fc23'
    auth_token = '1138af65d40e6e4207c886f03224b97d'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+13158884183',
        body='Your OTP password is ' + str(OTPcode),
        to='+91' + phonenumber
    )
    return OTPcode



# for signup of user...........
def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=name):
            messages.error(request,'user allready exist ..')
            # return HttpResponse('username is allready exist')
        elif customuser.objects.filter(mobile=mobile):
            messages.error(request,'mobile no allready registered..')
            # return HttpResponse('mobile no allready registered')
        else:
            otp=sendotp(mobile)
            user=User(username=name,first_name=name,email=email)
            cust=customuser(mobile=mobile,otp=otp)
            cust.save()
            request.session['mobileotp']=mobile
            request.session['username']=name
            request.session['email']=email
            request.session['password']=password
            return redirect('otp')

    return render(request,'signup.html')



def varifyotp(request):
    if request.method=='POST':
        motp=request.POST['sentmobileotp']
        mob=request.session['mobileotp']
        customuserobject=customuser.objects.get(mobile=mob)
        databaseotp=customuserobject.otp
        print(databaseotp)
        if databaseotp==motp:
            username=request.session['username']
            first_name=request.session['username']
            email=request.session['email']
            password=request.session['password']
            user=User(username=username,first_name=first_name,email=email,password=make_password(password))
            user.save()
            update_session_auth_hash(request,user)

        else:
            messages.error(request,'otp did not match..')
        return redirect('profile')
    return render(request,'otp.html')


@login_required
def profile(request):
    return render(request,'profile.html')



# for login to account........
def signin(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        x=authenticate(username=name,password=password)
        if x is not None:
            login(request,x)
            return redirect('profile')
        else:
            messages.error(request,'usename or password is in correct..')
    return render(request,'signin.html')



# for logout from account.......
def mylogout(request):
    logout(request)
    return redirect('signin')