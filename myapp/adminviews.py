from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth


def supervisor(request):
    if request.method =='POST':
        username =request.POST['username']
        password =request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if  user is not None:
            if user.is_staff:
              auth.login(request,user)
              return redirect ("dashboard")
            else:
              messages.info(request,'You are not authorized  to  access this page.')
              return redirect('supervisor')
        else:
          messages.info(request, 'You are not authorized  to  access this page.')
          return redirect('supervisor')
    else:
        return render(request,'adminlogin.html')
    

def logout(request):
    auth.logout(request)
    return redirect(supervisor)