from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User


# Create your views here.

def welcome(request):

    #we have to check the method that is sent throught the form
    #we are expecting twon method , get/post
    #get: user is viweing a simle html page
    #Post: user  send data through a form 

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user =  authenticate(request,username=username, password=password)
        #user entered the right credentials
        if user is not None:   
            login(request, user)
            return redirect('dashboard')
        else:
            print("hi , you have enterd wrong credentials") 
    else:
        return render(request,'login.html')


def dashboard(request):

    return render(request, 'dashboard.html')        



                                



