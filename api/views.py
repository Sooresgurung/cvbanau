from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url='login')
def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')


        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not same !!1")
        
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

# @login_required(login_url='logout')
def logIn(request):
    data = {'wrong':'User and password is not match',
            "msg":"Username and password is not correct!!!"}
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request,username=uname,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('./cv')
        else:
            return render(request,'login.html',data)

    return render(request,'login.html')

@login_required(login_url='login')
def logOut(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def cv(request):
    data  = CVform.objects.all()
    context = {'data':data}
    return render(request,'cv.html', context)


def cvform(request):
     if request.method == 'POST':
        uname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        clz = request.POST.get('clz_name')
        interest = request.POST.get('interest')
        skill = request.POST.get('skill')
        summary = request.POST.get('summary')
        profile = request.POST.get('profile_pic')
        my_cv = CVform( name=uname,email=email,phone=phone,clz_name=clz,interest=interest,skill=skill,summary=summary,profile_pic=profile)
        my_cv.save()

        return redirect('./cv')

     return render(request,'cvform.html')

    
    







