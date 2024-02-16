from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
import datetime
from .models import *

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def userreg(request):
    return render(request,'userreg.html')

def adduser(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        address=request.POST.get('address')
        
        cus=userregistartion(name=name,email=email,phone=phone,address=address,password=password)
        cus.save()
    return render(request,'index.html', {'message1':'successfully Registered'})




def login(request):
    return render(request,'login.html')

def addlogin(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    if username == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = username
        request.session['admin'] = 'admin'
        return render(request,'index.html')

    elif userregistartion.objects.filter(email=username,password=password).exists():
        userdetails=userregistartion.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id

            return render(request,'index.html')

    
    
   
    
    else:
        return render(request, 'login.html',{'success':'Invalid email id or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)
    
    
    
    
def addques(request):
    return render(request,'question.html')