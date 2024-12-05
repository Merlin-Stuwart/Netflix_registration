from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth,messages
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                #messages.info(request,'Email alrady taken')
                return HttpResponse('<center><h1>Email already taken</h1></center>')
                #return redirect('/registration')
            elif User.objects.filter(username=username).exists():
                # messages.info(request,'Username alrady taken')
                # return redirect('/registration')
                return HttpResponse('<center><h1>Username alrady taken</h1></center>')
            else:
                user =User.objects.create_user(username=username,email=email,password=password)
                user.save()
                
                return HttpResponse('<center><h1>Registrsation successful</h1></center>')
                
        else:
            return HttpResponse('<center><h1>Password is Not matching</h1></center>')
            #messages.info(request,'Password is Not Matching')
            #return redirect('/registration')
        
    else:
        return render(request,'registration.html')

    
def login(request):
    if request.method == 'POST':
        username = request.POST['un']
        password = request.POST['pw']
        user = authenticate(username=username,password=password)
        if user and user.is_active: 
            auth.login(request,user)
            return redirect('home')
        else:
            # messages.info(request,'Credentials Invalid !!')
            return HttpResponse('<center><h1 style=bacgground-color=wheat>Invalid user</h1></center>')
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))