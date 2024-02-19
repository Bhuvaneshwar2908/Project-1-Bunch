from email.mime import image
from tkinter import Image
from django.shortcuts import redirect,render
from contextlib import _RedirectStream,redirect_stderr
import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth




# Create your views here.


def home(requests):
    return render(requests,'home.html')

#def home(requests):
 #   return render(requests,'login.html')

def login(requests):
    if requests.method=='POST':
        username = requests.POST['username']
        password = requests.POST['password']
        user = auth.authenticate(username=username,password=password)
        user.save()
        #login(requests,user)
        print("user login done")
        return redirect('home/')
    else:
        return render(requests,'login.html')

def register(requests):
    if requests.method == 'POST':
        fullname = requests.POST['fullname'] 
        username = requests.POST['username']
        email = requests.POST['email']
        phonenumber=requests.POST['phone number']
        password = requests.POST['password']
        confirmpassword = requests.POST['confirmpassword']
        gender = requests.POST['gender']

        user=user.objects.create_user(fullname=fullname,username=username,email=email,phonenumber=phonenumber,password=password,confirmpassword=password,gender=gender)
        user.save()

        print('successfully registered')
        return redirect('/')
    else:
        return render(requests,'register.html')

def dasboard(requests):
    return render(requests,'dashboard.html')
