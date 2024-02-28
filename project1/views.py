from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# the Destination model made using a class in models.py which is a model
# Create your views here.
def index(request):
  dests=Destination.objects.all()
  return render(request,"index.html",{'dests':dests})

def register(request):
  if(request.method=='POST'):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    username=request.POST['username']
    email=request.POST['email']
    password1=request.POST['password1']
    password2=request.POST['password2']
    if password1==password2:
      if User.objects.filter(username=username).exists():
        messages.info(request,'username taken')
        return redirect('register')
      else:
        user=User.objects.create_user(username=username,email=email,password=password1,first_name=firstname,last_name=lastname)
        user.save()
        messages.info(request,'user created')
        return redirect('login')
    messages.info(request,'password not same')
    return redirect('register')

  
  else:
    return render(request,"register.html")
def login(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('/')
    else:
      messages.info(request,"invalid credentials")
      return redirect('login')
  else:
    return render(request,"login.html")
def logout(request):
  auth.logout(request)
  return redirect('/')

@login_required
def if_logged_in_only(request):
  return render(request,'if_logged_in_only.html')